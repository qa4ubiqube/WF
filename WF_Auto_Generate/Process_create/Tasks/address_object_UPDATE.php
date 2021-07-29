<?php

require_once '/opt/fmc_repository/Process/Reference/Common/common.php';

function list_args()
{
  create_var_def('device_id', 'Device');
  create_var_def('address_object.0.object_id', 'String');
create_var_def('address_object.0.addressBookName', 'ObjectRef');
create_var_def('address_object.0.addressNetworkIP', 'IpAddress');
create_var_def('address_object.0.addressNetworkPrefix', 'Integer');
create_var_def('address_object.0.addressNetworkMask', 'IpAddress');
create_var_def('address_object.0.addressRangeFirstIP', 'IpAddress');
create_var_def('address_object.0.addressRangeLastIP', 'IpAddress');
create_var_def('address_object.0.addressDnsName', 'String');
create_var_def('address_object.0.addressIPv4onlyOption', 'String');
create_var_def('address_object.0.addressIPv6onlyOption', 'String');
create_var_def('address_object.0.ipv6-only', 'String');
create_var_def('address_object.0.ipv4-only', 'String');
create_var_def('address_object.0.addressDescription', 'String');

}

check_mandatory_param('device_id');

$device_id = $context['device_id'];
$prefix = substr($device_id, 0, 3);
$device_id = str_replace($prefix, '', $device_id);

foreach ($context['address_object'] as $key => $value) {
   $object_parameters['address_object'][$value['object_id']] = $value;
}


$response = execute_command_and_verify_response($device_id, "UPDATE", $object_parameters, "UPDATE address_object");
  $response = json_decode($response, true);
if ($response['wo_status'] !== ENDED) {
	$response = prepare_json_response($response['wo_status'], $response['wo_comment'], $context, true);
	echo $response;
	exit;
}

$response = prepare_json_response(ENDED, "order command execute successfull", $response['wo_newparams'], true);
echo $response;
?>
