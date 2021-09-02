'''
Visit http://[YOUR_MSA_URL]/msa_sdk/ to see what you can import.
'''
import random
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

dev_var = Variables()
dev_var.add('spreadsheet_list.0.spreadsheet', var_type='String')
dev_var.add('spreadsheet_list.0.is_selected', var_type='Boolean')
dev_var.add('spreadsheet_list.0.device_external_ref', var_type='String')
dev_var.add('spreadsheet_list.0.device_hostname', var_type='String')
context = Variables.task_call(dev_var)
context['var_name2'] = 100
#if (random.randint(1,10) % 2):
#    ret = MSA_API.process_content('FAIL', 'Task FAIL' , context, True)
#else:
ret = MSA_API.process_content('ENDED', 'Task OK' , context, True)
print(ret)

