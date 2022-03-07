import sys
import subprocess
import re

from msa_sdk.variables import Variables
from msa_sdk.msa_api import MSA_API

dev_var = Variables()
dev_var.add('import_mibs_path', var_type='String')
dev_var.add('mibs_name.0.name', var_type='String')
dev_var.add('mibs_name.0.selected', var_type='Boolean')

context = Variables.task_call(dev_var)

oid_startswith_filter_list = ('0.')

if not 'mibs_name' in context:
    ret = MSA_API.process_content('WARNING', 'No MIB to import', context, True)
    print(ret)
    sys.exit(0)

if not 'mibs_path' in context:
    ret = MSA_API.process_content('WARNING', 'No path where to import MIBs', context, True)
    print(ret)
    sys.exit(0)

selected_mibs_name = []
for mibs in context['mibs_name']:
    if 'selected' in mibs and mibs['selected'] == True:
        selected_mibs_name.append(mibs['name'])

if not selected_mibs_name:
    ret = MSA_API.process_content('WARNING', 'No MIB selected', context, True)
    print(ret)
    sys.exit(0)

'''
Parse the MIBs
    Translate OID names in OIDs thanks to snmptranslate CLI
    Build the dictionary oid_list with key = oid, value = oid name
    to ensure the uniqueness of the oid
'''
oid_list = {}
mib_path_str = ':'.join(context['mibs_path'])
mib_name_str = ':'.join(selected_mibs_name)
cmd = ['/usr/bin/snmptranslate', '-Pu', '-Tz', '-M', mib_path_str, '-m', mib_name_str]
# for python >= 3.7 replace universal_newlines by text
proc = subprocess.run(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True)
if proc.returncode == 0:
    # each line of out is like "oid name" "oid"
    out = proc.stdout
    pattern = '^\s*"([^"]+)"\s+"([^"]+)"'
    regc = re.compile(pattern, flags = re.MULTILINE)
    result = regc.findall(out)
    if result != None:
        # result is a list of tuple, each tuple is a (oid_name, oid) pair
        for name, oid in result:
            if not oid.startswith(oid_startswith_filter_list):
                if not oid in oid_list:
                    oid_list[oid] = name

'''
Build a tree  in the dictionary oid_tree to identify leaves
'''
oid_tree = {}
def add_node(tree, oid, name):
    new_tree = cur_tree = tree
    for item in oid.split('.'):
        if item not in cur_tree:
            cur_tree[item] = {}
        cur_tree = cur_tree[item]
    return new_tree

for oid, name in oid_list.items():
    oid_tree = add_node(oid_tree, oid, name)

'''
Get leaves from the tree oid_tree
and store them in a dictionary
'''
leaf_list= {}
oid = ''
def get_leaves(tree, oid, leaves):
    cur_oid = oid
    cur_leaves = leaves
    for key, value in tree.items():
        if oid:
            cur_oid = oid + '.' + key
        else:
            cur_oid = key
        if value:
            cur_leaves = get_leaves(value, cur_oid, cur_leaves)
        else:
            cur_leaves[cur_oid] = True
    return cur_leaves

leaf_list = get_leaves(oid_tree, oid, leaf_list)

'''
Get existing translated OIDs if any
'''
translated_oid_list = {}
dst_file = context['translated_oid_file_name']
try:
    with open(dst_file, 'r') as f:
        for line in f:
            oid, name = line.split()
            translated_oid_list[oid] = name
except:
    pass

'''
Build a new dictionary for the WF task
with leaves only and already translated OIDs if any
'''
imported_oid_list = []
for oid, name in oid_list.items():
    if oid in leaf_list:
        if oid in translated_oid_list:
            imported_oid_list.append({'oid': oid, 'oid_name': name, 'selected': True})
        else:
            imported_oid_list.append({'oid': oid, 'oid_name': name, 'selected': False})

for oid, name in translated_oid_list.items():
    if not oid in leaf_list:
        imported_oid_list.append({'oid': oid, 'oid_name': name, 'selected': True})

context['imported_oids'] = imported_oid_list

imported_mib = ', '.join(selected_mibs_name)
if len(imported_mib) > 64:
    imported_mib = imported_mib[:64] + '...'
imported_mib_nb = len(selected_mibs_name)
context['import_summary'] = f'Total {imported_mib_nb} : {imported_mib}'

ret = MSA_API.process_content('ENDED', 'Import OK', context, True)
print(ret)

