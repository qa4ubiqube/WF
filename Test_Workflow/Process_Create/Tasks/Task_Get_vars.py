'''
Visit http://[YOUR_MSA_URL]/msa_sdk/ to see what you can import.
'''
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

import requests
headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(Variables.task_call()['TOKEN']),
        }
res = requests.get('http://localhost:8480/ubi-api-rest/system-admin/v1/msa_vars?name='.format('UBI_SMTP_IPADDR'))

print(res)


ret = MSA_API.process_content('ENDED', 'Task OK ' + res.json(), context, True)
print(ret)

