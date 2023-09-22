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
##dev_var.add('file_uri', var_type='String')
context = Variables.task_call(dev_var)

RepositoryObject = Repository()
  

workflow_definition =  ''' {
  "example": {
    "content": "string"
  },
  "metaInformationList": [
    {
      "type": "FILE",
      "name": "TESTb44.xml",
      "displayName": "TESTb44",
      "repositoryName": "Process",
      "parentURI": "Process/workflows/TESTb44",
      "fileType": "text",
      "tag": "string",
      "comment": "string",
      "modelId": 0,
      "vendorId": 0,
      "uri": "Process/workflows/TESTb44/TESTb44.xml",
      "file": "true"
    }
  ],
  "information": {
    "displayName": "TESTb44",
    "icon": "string",
    "description": "TESTb44",
    "category": "string",
    "displayField": "string",
    "serviceTaskType": "string",
    "order": 0,
    "visibility": "5"
  },
  "process": [
    {
      "name": "Process/workflows/TESTb44/create",
      "displayName": "instanciate",
      "type": "CREATE",
      "visibility": "5",
      "allowSchedule": false,
      "tasks": [
        {
          "fileName": "Task1.py",
          "fileUri": "/opt/fmc_repository/Process/workflows/TESTb44/Process_instanciate/Tasks",
          "displayName": "Task1"
        }
      ]
    }
  ]
} 
'''


context['workflow_definition_new'] = workflow_definition

workflow_definition_dict = json.loads(workflow_definition)  #convert string into dict
context['workflow_definition_dict'] = str(workflow_definition_dict)
file_uri =  'Process/workflows/TESTb44/TESTb44.xml' 

context['workflow_definition_string'] = json.dumps(workflow_definition_dict)


RepositoryObject.create_workflow_definition(workflow_definition_dict)
response = json.loads(RepositoryObject.content)
context['repo_response']= str(response)

if (response.get('wo_status') and (response.get('wo_status') =='FAILED' or response.get('wo_status') == 'FAIL')):
  MSA_API.task_error('Error, For '+file_uri+', response=' + str(RepositoryObject.content), context, True)
else:
  #IF OK, there is no 'wo_status' in the response
  MSA_API.task_success('Task OK for '+file_uri+', response=' + str(RepositoryObject.content), context, True)