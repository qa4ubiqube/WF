<?php

require_once '/opt/fmc_repository/Process/Reference/Common/common.php';

function list_args()
{
  create_var_def('device_id', 'Device');
  create_var_def('bgp_neighbour.0.address_family_row', 'String');
create_var_def('bgp_neighbour.0.object_id', 'String');
create_var_def('bgp_neighbour.0.asn', 'String');
create_var_def('bgp_neighbour.0.peer_group', 'String');
create_var_def('bgp_neighbour.0.router_id', 'String');
create_var_def('bgp_neighbour.0.state', 'String');
create_var_def('bgp_neighbour.0.address_family.0.afi', 'String');
create_var_def('bgp_neighbour.0.address_family.0.safi', 'String');
create_var_def('bgp_neighbour.0.vrf', 'OBMFRef');
create_var_def('bgp_neighbour.0.local_asn', 'OBMFRef');

}

check_mandatory_param('device_id');

$device_id = $context['device_id'];
$prefix = substr($device_id, 0, 3);
$device_id = str_replace($prefix, '', $device_id);

foreach ($context['bgp_neighbour'] as $key => $value) {
   $object_parameters['bgp_neighbour'][$value['object_id']] = $value;
}


$response = execute_command_and_verify_response($device_id, "UPDATE", $object_parameters, "UPDATE bgp_neighbour");
  $response = json_decode($response, true);
if ($response['wo_status'] !== ENDED) {
	$response = prepare_json_response($response['wo_status'], $response['wo_comment'], $context, true);
	echo $response;
	exit;
}

$response = prepare_json_response(ENDED, "order command execute successfull", $response['wo_newparams'], true);
echo $response;
?>
