from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order
from msa_sdk.orchestration import Orchestration
from msa_sdk.device import Device
from msa_sdk.conf_backup import ConfBackup
from msa_sdk import constants
import json

dev_var = Variables()                           

dev_var.add('services_to_search')
dev_var.add('service_instance_id')
dev_var.add('service_external_reference')
dev_var.add('process_instance_id')
dev_var.add('service_execution_status')
dev_var.add('service_variables')

context = Variables.task_call(dev_var)

context['services_to_search'] = ["Process/Helloworld/Helloworld"]
context['service_instance_id'] = 0
context['service_external_reference'] = ''
context['process_instance_id'] = 0
context['service_execution_status'] = ''
context['service_variables'] = [
	{
		"variable":"service_id",
		"operator":">",
		"value":"0",
		"nextConditionJoinOperator":""
	}
	# {
	# 	"variable":"var_name",
	# 	"operator":"=",
	# 	"value":"666",
	# 	"nextConditionJoinOperator":""
	# }
]

Orchestration = Orchestration(context['UBIQUBEID'])

result = Orchestration.read_service_instance_by_condition(context['services_to_search'],
context['service_instance_id'],context['service_external_reference'],
context['process_instance_id'],context['service_execution_status'],
context['service_variables'])

context['final_result'] = json.loads(result)[0]['name']

ret = MSA_API.process_content('ENDED', "DONE", context, True)
print(ret)