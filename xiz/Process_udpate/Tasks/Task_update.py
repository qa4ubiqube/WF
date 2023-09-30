
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

dev_var = Variables()
dev_var.add('var_name', var_type='String')
dev_var.add('var_name2', var_type='Integer')

context = Variables.task_call(dev_var)
context['var_name2'] = int(context['var_name2']) + 1

ret = MSA_API.process_content('ENDED', 'Cloudclapp', context, True)
print(ret)

