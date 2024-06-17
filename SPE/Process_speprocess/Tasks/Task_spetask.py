'''
Visit http://[YOUR_MSA_URL]/msa_sdk/ to see what you can import.
'''
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API


dev_var = Variables()
dev_var.add('var_1.0.tab', var_type='String')
dev_var.add('var_1.0.tab2', var_type='String')
dev_var.add('var_1.0.tab2.0.test', var_type='String')
dev_var.add('var_1.0.tab2.0.test2', var_type='String')
dev_var.add('var_1.0.tab2.0.test3.0.tzt', var_type='String')


context = Variables.task_call(dev_var)

ret = MSA_API.process_content('ENDED', 'Task OK', context, True)
print(ret)

