'''
Visit http://[YOUR_MSA_URL]/msa_sdk/ to see what you can import.
'''
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.util import get_vars_value

import requests

res = get_vars_value('UBI_SMTP_IPADDR666')
context = Variables.task_call()
ret = MSA_API.process_content('ENDED', 'Task OK ' + res, context, True)
print(ret)

