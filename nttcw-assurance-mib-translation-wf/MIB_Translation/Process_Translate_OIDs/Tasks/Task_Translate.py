import sys
import os

from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

dev_var = Variables()
dev_var.add('imported_oids.0.oid_name', var_type='String')
dev_var.add('imported_oids.0.oid', var_type='String')
dev_var.add('imported_oids.0.selected', var_type='Boolean')

context = Variables.task_call(dev_var)

if not 'imported_oids' in context:
    ret = MSA_API.process_content('WARNING', 'No OID to translate', context, True)
    print(ret)
    sys.exit(0)

'''
Generate a string where each line is composed of a pair
oid oid_name
'''
imported_oid_list = context['imported_oids']
oid_str = ''

for oid_obj in imported_oid_list:
    if 'selected' in oid_obj:
        if oid_obj['selected']:
            oid_str += '{} {}\n'.format(oid_obj['oid'], oid_obj['oid_name'])

'''
Store selected oid in a temporary file
'''
dst_file = context['translated_oid_file_name']
tmp_file = dst_file + '.tmp'

with open(tmp_file, 'w') as f:
    f.write(oid_str)

'''
Move the temporary file into a final one
'''
os.rename(tmp_file, dst_file)

ret = MSA_API.process_content('ENDED', f'MIB translation completed\nFile created: {dst_file}', context, True)
print(ret)

