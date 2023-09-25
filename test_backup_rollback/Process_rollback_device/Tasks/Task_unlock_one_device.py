import json
import time
import ipaddress
import os
from msa_sdk.variables import Variables
from msa_sdk import constants
from msa_sdk import util
from msa_sdk.msa_api import MSA_API

dev_var = Variables()
context = Variables.task_call(dev_var)
 
device_name_IP            = context['device_name_IP']
lock_file_name            = device_name_IP
lock_file_name            = context['lock_file_name']
mode                      = 'w+'
process_param             ={}
process_param['process']           = 'test'
sleep_time=30
max_try_nb=10
sleep_time=10
max_try_nb=5

#Release lock file.
result = util.release_file_lock_exclusif(lock_file_name, process_param, sleep_time, max_try_nb)
result = json.loads(result)
if result.get('wo_status') and result['wo_status'] != 'ENDED' and result.get('wo_comment'): 
  MSA_API.task_error('OPERATION FAILED, File "'+lock_file_name+'" not unlocked : '+result['wo_comment'],context, True)
 
MSA_API.task_success('OPERATION ENDED, File "'+lock_file_name+'" unlocked : '+result['wo_comment'],context, True)
