'''
Visit http://[YOUR_MSA_URL]/msa_sdk/ to see what you can import.
'''
import json
import time
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.device import Device
from msa_sdk.repository import Repository

dev_var = Variables()
dev_var.add('file_uri', var_type='String')
context = Variables.task_call(dev_var)

RepositoryObject = Repository()

file_uri = context['file_uri']  # 'Process/workflows/TEST_ARRAY_ARRAY/TEST_ARRAY_ARRAY.xml';

RepositoryObject.delete_workflow_definition(file_uri)
if RepositoryObject.content:
  response = json.loads(RepositoryObject.content)
  if (response.get('wo_status') and (response.get('wo_status') =='FAILED' or response.get('wo_status') == 'FAIL')):
    MSA_API.task_error('Error, to delete Workflow "'+file_uri+'", response=' + str(RepositoryObject.content), context, True)
  else:
    #IF OK, there is no 'wo_status' in the response
    MSA_API.task_success('Task OK, Workflow "'+file_uri+'" deleted, response=' + str(RepositoryObject.content), context, True)

else:
  #IF OK, there is no   response
  MSA_API.task_success('Task OK, Workflow "'+file_uri+'" deleted', context, True)
