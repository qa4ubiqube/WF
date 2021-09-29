'''
Visit http://[YOUR_MSA_URL]/msa_sdk/ to see what you can import.
'''
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

MSA_API._init_()
MSA_API.path = 'system-admin/v1/msa_vars?name={}'.format('UBI_SMTP_IPADDR')
res = MSA_API._call_get()



ret = MSA_API.process_content('ENDED', 'Task OK ' + res, context, True)
print(ret)

