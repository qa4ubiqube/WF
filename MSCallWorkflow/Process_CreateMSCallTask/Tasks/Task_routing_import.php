<?php

require_once '/opt/fmc_repository/Process/Reference/Common/common.php';

function list_args()
{
  create_var_def('device_id', 'Device');
  
}

check_mandatory_param('device_id');

$device_id = $context['device_id'];
$device_id = getIdFromUbiId ($device_id);

$object_parameters['static_route'] = '0';


$response = execute_command_and_verify_response($device_id, "IMPORT", $object_parameters, "IMPORT static_route");
  $response = json_decode($response, true);
if ($response['wo_status'] !== ENDED) {
	$response = prepare_json_response($response['wo_status'], $response['wo_comment'], $context, true);
	echo $response;
	exit;
}

$response = prepare_json_response(ENDED, "order command execute successfull", $response['wo_newparams'], true);
echo $response;
?>
