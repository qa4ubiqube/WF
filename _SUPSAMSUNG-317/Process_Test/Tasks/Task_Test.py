#################################################################
import json
import os
import sys
import uuid
from msa_sdk.msa_api import MSA_API
from msa_sdk.variables import Variables
import requests
import logging


dev_var = Variables()
dev_var.add("me_inventory_id", var_type="Device")
dev_var.add("subtenant_inventory_id", var_type="Subtenant")
dev_var.add("central_subtenant_inventory_id", var_type="Subtenant")
dev_var.add("vni", var_type="Integer")
dev_var.add("vni_name", var_type="String")
dev_var.add("use_fabric_vlan", var_type="Boolean")
dev_var.add("vlan", var_type="String")
dev_var.add("vlan_name", var_type="String")
dev_var.add("description", var_type="String")
dev_var.add("replication_mode", var_type="String")
dev_var.add("rd", var_type="String")
dev_var.add("rt_import", var_type="String")
dev_var.add("rt_export", var_type="String")
dev_var.add("mtu", var_type="Integer")
dev_var.add("l2only", var_type="Boolean")
dev_var.add("arp_suppression", var_type="Boolean")
dev_var.add("vrf_instance_id", var_type="String")
dev_var.add("gateway_list.0.ip_address", var_type="String")
dev_var.add("gateway_list.0.type", var_type="String")
dev_var.add("dhcp_relay_servers.0.ip_address", var_type="IpAddress")
dev_var.add("dhcp_relay_servers.0.vrf_name", var_type="String")
#dev_var.add("members.0.device", var_type="Device", values= values)
dev_var.add("members.0.device", var_type="String")
dev_var.add("members.0.switch_instance_id")
dev_var.add("members.0.switch_name", var_type="String")
dev_var.add("members.0.switch_role", var_type="String")
dev_var.add("members.0.serial_number", var_type="String")
dev_var.add("members.0.vlan", var_type="Integer")
dev_var.add("members.0.interfaces.0.name", var_type="String")
dev_var.add("members.0.interfaces.0.vlan_mode", var_type="String")
dev_var.add("members.0.interfaces.0.description", var_type="String")
dev_var.add("test", var_type="String")
context=Variables.task_call(dev_var)

"""
#########################PYTHON-PRE-TASK-START###########################
import requests
import json
import logging
import sys
import urllib3

'''
urllib3.disable_warnings()
http_logger = logging.getLogger("urllib3")
http_logger.setLevel(logging.DEBUG)
http_handler = logging.FileHandler('/tmp/example.log')
http_handler.setLevel(logging.DEBUG)
http_logger.addHandler(http_handler)

logging.basicConfig(filename='/tmp/example.log', encoding='utf-8', level=logging.DEBUG)

# add console output in addition to the log file
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')
'''

URL_TOKEN="http://localhost:8480/ubi-api-rest/auth/token"

headers = {
    'Content-Type': 'application/json'
}
data = {
    'username': 'ncroot',
    'password': 'ubiqube'
}

response = requests.post(URL_TOKEN, headers=headers, json=data)
token_url_response=response.json()
token=token_url_response.get('token')
#logger.info('Print test 1')
#logger.info(token)

URL="http://localhost:8480/ubi-api-rest/lookup/v1/customer/26/devices"
results=[]
auth_token = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJuY3Jvb3QiLCJpYXQiOjE2ODgzNzY1NjcsImx2bCI6IjEiLCJleHAiOjE3MDEzMzY1Njd9.WKyVxAx1-q-ZEyfTtlwDdB7Qsb4KsSjypJT_9FAJGFrgvAhAMNwg04j_VQQJ7vEz1ykn5aLbPUN2Abv5Nwt0KQ"

#response = requests.get(URL, headers={'authorization': 'Bearer '+token })
response = requests.get(URL, headers={'authorization': 'Bearer '+$auth_token })
data = response.json()

values=[]
for device in data:
  new_dict={
    'displayValue' : device['name'],
    'actualValue': device['id']
    
  }
  values.append(new_dict)

#uniqueItemsInDropDownList = {'uniqueItemsInDropDownList': 'true'}
results.append({'members.0.device': values})
#results.append({'members.0.device': uniqueItemsInDropDownList})

print(json.dumps(results))
#####################PYTHON-PRE-TASK-END#################
"""
ret = MSA_API.process_content('ENDED', 'Task OK', context, True)
print(ret)