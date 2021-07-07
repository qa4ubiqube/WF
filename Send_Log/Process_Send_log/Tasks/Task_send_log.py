from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from datetime import datetime
import json
import requests

dev_var = Variables()
dev_var.add('message', var_type='String')
dev_var.add('severity', var_type='Integer')
dev_var.add('device_id', var_type='Device')
dev_var.add('subtenant_id', var_type='Customer')

context = Variables.task_call(dev_var)

dateTimeObj = datetime.now()
format = "%Y-%m-%dT%H:%M:%S+0000"
time1 = dateTimeObj.strftime(format)
format = "%Y-%m-%d"
date = dateTimeObj.strftime(format)

url = "http://msa_es:9200/ubilogs-"+date+"/_doc"

severity = context['severity']
rawlog = context['message']
device_id = context['device_id']
customer_ref = context['subtenant_id']

payload = {"rawlog": ""+rawlog+"", "device_id": ""+device_id+"", "date": ""+time1+"", "customer_ref": ""+customer_ref+"", "severity": ""+severity+"", "type": "NOTIFICATION", "subtype": "WF"}

headers = {'content-type': 'application/json'}

r = requests.post(url, json=payload, headers=headers)

ret = MSA_API.process_content('ENDED', url, context, True)
print(ret)