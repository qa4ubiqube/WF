import json
import time
import ipaddress
import os
import sys
from msa_sdk.variables import Variables
from msa_sdk import constants
from msa_sdk.msa_api import MSA_API
currentdir = os.path.dirname(os.path.realpath(__file__))
lib_dir  = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(lib_dir)
from common.common import *


dev_var = Variables()
dev_var.add('device_id')
context = Variables.task_call(dev_var)
 
device_list = context['device_list'] 


device_list = do_rollback(device_list, 300)
context['device_list'] = device_list
restore_error=[]
for device in device_list:
  if device.get('rollback_result').get('status') != constants.ENDED:
    restore_error.append(device['id']+':'+str(device.get('rollback_result')))

if restore_error:
  MSA_API.task_error('Can not restore devices : "'+' ,'.join(restore_error) +'"',context, True)

MSA_API.task_success('OPERATION ENDED, device backup done , resultat=' +str(device_list),context, True)
