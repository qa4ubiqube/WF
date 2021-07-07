import json
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order

# List all the parameters required by the task
dev_var = Variables()
dev_var.add('device_id', var_type='Device')
dev_var.add('hto_list_file.0.object_id', var_type='String')
dev_var.add('hto_list_file.0.lnk', var_type='String')
dev_var.add('hto_list_file.0.mod', var_type='String')
dev_var.add('hto_list_file.0.permission.0.read', var_type='Boolean')
dev_var.add('hto_list_file.0.permission.0.write', var_type='Boolean')
dev_var.add('hto_list_file.0.permission.0.execute', var_type='Boolean')
dev_var.add('hto_list_file.0.size', var_type='AutoIncrement')
dev_var.add('hto_list_file.0.group', var_type='String')
dev_var.add('hto_list_file.0.owner', var_type='AutoIncrement')
dev_var.add('hto_list_file.0.timestamp', var_type='String')
dev_var.add('hto_list_file.0.content', var_type='String')
dev_var.add('hto_list_file.0.increment', var_type='AutoIncrement')
dev_var.add('hto_list_file.0.msRef', var_type='ObjectRef')

context = Variables.task_call(dev_var)

# read the ID of the selected managed entity
device_id = context['device_id']

# extract the database ID
devicelongid = device_id[3:]

# build the Microservice JSON params for IMPORT
#{"Gateway":"0"}
#micro_service_vars_array = {"object_id":object_id}
object_parameters = {}

object_parameters['hto_list_file'] = {}
for v in context['hto_list_file']:
  object_parameters['hto_list_file'][v['object_id']] = v


# call the CREATE for simple_firewall MS for each device
order = Order(devicelongid)
order.command_execute('CREATE', object_parameters)

# convert dict object into json
content = json.loads(order.content)

# check if the response is OK
if order.response.ok:
    ret = MSA_API.process_content('ENDED',
                                  f'STATUS: {content["status"]}, \
                                    MESSAGE: successfull',
                                  context, True)
else:
    ret = MSA_API.process_content('FAILED',
                                  f'Import failed \
                                  - {order.content}',
                                  context, True)


print(ret)

