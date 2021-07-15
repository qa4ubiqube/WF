from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
import sys

dev_var = Variables()
context = Variables.task_call(dev_var)
dev_var = Variables()
dev_var.add('var_name', var_type='String') 

ret = MSA_API.process_content('PAUSE', 'Task paused', context, True)
print(ret)
sys.exit()