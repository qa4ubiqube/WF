import json
from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API
from msa_sdk.order import Order

# List all the parameters required by the task
dev_var = Variables()
dev_var.add('device_id', var_type='Device')
dev_var.add('access_lists.0.object_id', var_type='String')
dev_var.add('access_lists.0.acl.0.condition', var_type='String')
dev_var.add('access_lists.0.acl.0.protocol', var_type='String')
dev_var.add('access_lists.0.acl.0.src_address', var_type='String')
dev_var.add('access_lists.0.acl.0.src_address_host', var_type='String')
dev_var.add('access_lists.0.acl.0.any_src', var_type='String')
dev_var.add('access_lists.0.acl.0.src_wildcard', var_type='String')
dev_var.add('access_lists.0.acl.0.src_port', var_type='String')
dev_var.add('access_lists.0.acl.0.dst_address', var_type='String')
dev_var.add('access_lists.0.acl.0.dst_address_host', var_type='String')
dev_var.add('access_lists.0.acl.0.any_dst', var_type='String')
dev_var.add('access_lists.0.acl.0.dst_wildcard', var_type='String')
dev_var.add('access_lists.0.acl.0.dst_port', var_type='String')

context = Variables.task_call(dev_var)

# read the ID of the selected managed entity
device_id = context['device_id']

# extract the database ID
devicelongid = device_id[3:]

# build the Microservice JSON params for IMPORT
#{"Gateway":"0"}
#micro_service_vars_array = {"object_id":object_id}
object_parameters = {}

object_parameters['access_lists'] = {}
for v in context['access_lists']:
  object_parameters['access_lists'][v['object_id']] = v


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

