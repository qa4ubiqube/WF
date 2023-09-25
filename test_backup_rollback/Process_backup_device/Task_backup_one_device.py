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
 
device_id            = context['device_id']
device_list = []
device_list.append({"id": device_id})
context['device_list'] = device_list

result = backup_devices_configuration(device_list)
# result={"date" : "14-09-2022 15:04:59", "message" : "SMS-CMD-FAILED","result" : "","revisionId" : -1,"status" : "FAIL"}
#  result={"date" : "14-09-2022 15:08:00","message" : "BACKUP started","result" : "","revisionId" : -1,"status" : "RUNNING"

context['device_list'] = result

MSA_API.task_success('OPERATION ENDED, device backup done = "' + device_id  + '", result=' +str(result) ,context, True)
