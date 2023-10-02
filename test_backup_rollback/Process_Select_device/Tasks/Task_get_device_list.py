import json
import time
import ipaddress
import os
from msa_sdk.variables import Variables
from msa_sdk import constants
from msa_sdk.msa_api import MSA_API

dev_var = Variables()
dev_var.add('device_id')
context = Variables.task_call(dev_var)
 
device_id            = context['device_id']


MSA_API.task_success('OPERATION ENDED, device  = "' + device_id  + '" selectd',context, True)
