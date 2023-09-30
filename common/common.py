import json
import time
import ipaddress
import os
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order
from msa_sdk.device import Device
from msa_sdk.customer import Customer
from msa_sdk.orchestration import Orchestration
from msa_sdk.lookup import Lookup
from msa_sdk import constants
from msa_sdk.conf_backup import ConfBackup

dev_var = Variables()
context = Variables.task_call(dev_var)

MS_General_CDP_Neighbors = 'General_CDP_Neighbors'

# return type
#   IMPORT (only in valid case) : json.loads(order.content)['message']
#   OTHERS                      : []
def send_continuous_request_on_MS(command, devicelongid, MS, param, timeout = 180, interval = 15):
  order    = Order(devicelongid)
  global_timeout = time.time() + timeout

  while True:
    order.command_execute(command, param)
    content = json.loads(order.content)

    if order.response.ok:
      if command == 'IMPORT':
        context['import_result'] = content
        if "message" in content:
          import_result_message = json.loads(content['message'])
          if MS not in import_result_message:
            return {}
          return import_result_message
      return {}
    else:
      if time.time() > global_timeout:
        MSA_API.task_error(command + ' Microservice "'+MS+'" FAILED',context, True)
      time.sleep(interval)

def backup_devices_configuration(device_list):
  #TODO in parallele mode 5-10 device backup in same times)
  conf_backup=ConfBackup()
  for device in device_list : 
    devicelongid=device['id'][3:]
    context['result']=conf_backup.backup(devicelongid)
    context['backup_result']=conf_backup.content
    loop=1
    backup_result = '{"status": "FAILED"}'
    while loop < 15:
      time.sleep(5)
      status = conf_backup.backup_status(devicelongid)
      # backup_result  ={"date" : "14-09-2022 15:08:00","message" : "BACKUP started","result" : "","revisionId" : -1,"status" : "RUNNING"

      if status != constants.RUNNING :
         break
      loop = loop + 1
    device['backup_result'] = json.loads(conf_backup.content)
    
  return device_list


def do_rollback(device_list, time_out = 200):
  #backup_point='r1808'
  conf_backup=ConfBackup()
  interval_sec = 5 
  nb_loop_max = int (time_out / interval_sec)
  for device in device_list : 
    #device = {'id': 'INV695', 'backup_result': '{\n  "date" : "14-09-2022 15:42:49",\n  "message" : "BACKUP processed",\n  "result" : "",\n  "revisionId" : 2095,\n  "status" : "ENDED"\n}'}]
    devicelongid=device['id'][3:]
    rollback_result = '{"status": "FAILED"}'
    loop=0
    if device.get('backup_result') and device['backup_result'].get('revisionId'):
      revisionId = device['backup_result']['revisionId']
      context['result']=conf_backup.restore(devicelongid, revisionId)
      rollback_result = {"status": "FAILED"}
      while loop < nb_loop_max:
        time.sleep(interval_sec)
        conf_backup.restore_status(devicelongid)
        status =  json.loads(conf_backup.content)['status'] 
        # backup_result  ={"date" : "14-09-2022 15:08:00","message" : "BACKUP started","result" : "","revisionId" : -1,"status" : "RUNNING"
        if status and status != constants.RUNNING :
           break
        loop = loop + 1
    if loop < nb_loop_max:
      device['rollback_result'] = json.loads(conf_backup.content)
    else:
      #timeout
      device['rollback_result'] = json.loads(conf_backup.content)
      device['rollback_result']['TIMEOUT'] = ' do_rollback TIMEOUT >'+str(time_out)+' secs '
  return device_list

'''
def find_direct_neighbors_for_one_device(device_id):
  global MS_General_CDP_Neighbors
  # Task_Get_Device_Neighbours_List.py
  devicelongid = device_id[3:]
  order = Order(devicelongid)

  ms_input = {}
  ms_input['object_id'] = 'default' #need at least on value
  obj = {}
  obj['need_for_import'] = ms_input
  params = {}
  params[MS_General_CDP_Neighbors] = obj
  # IMPORT ONLY the MS MS_General_CDP_Neighbors
  order.command_execute('IMPORT', params, 120)
  # convert dict object into json
  response = json.loads(order.content)
  #context['direct_neighbor_response_'+device_id] = response

  if (response.get("status") and response["status"] == "OK" or response.get("wo_status") and response["wo_status"] == "OK"):
    if response.get("status"):
      message = response["message"]
    else:
      message = response["wo_new_params"]
    message = json.loads(message)
    #context['direct_neighbor_'+device_id] = message
    if message.get(MS_General_CDP_Neighbors):
      # "message": "{"General_CDP_Neighbors":{"eth1/8":{"object_id":"eth1/8","neighbor_system_name":"leaf-06","neighbor_interface":"eth1/8","management_ip":"192.168.130.106"},"eth1/3":{"object_id":"eth1/3","neighbor_system_name":"Spine-03","neighbor_interface":"eth1/1","management_ip":"192.168.130.203"},"mgmt0":{"object_id":"mgmt0","neighbor_system_name":"Spine-03","neighbor_interface":"mgmt0","management_ip":"192.168.130.203"},"eth1/9":{"object_id":"eth1/9","neighbor_system_name":"leaf-06","neighbor_interface":"eth1/9","management_ip":"192.168.130.106"},"eth1/4":{"object_id":"eth1/4","neighbor_system_name":"Spine-04","neighbor_interface":"eth1/1","management_ip":"192.168.130.204"}}}",
      return message[MS_General_CDP_Neighbors]
  return '{}'

'''

