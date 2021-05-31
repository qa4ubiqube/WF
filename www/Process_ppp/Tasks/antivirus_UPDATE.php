<?php

require_once '/opt/fmc_repository/Process/Reference/Common/common.php';

function list_args()
{
  create_var_def('device_id', 'Device');
  create_var_def('antivirus.0.object_id', 'String');
create_var_def('antivirus.0.scanbotnet', 'String');
create_var_def('antivirus.0.protocols_0_protocol', 'String');
create_var_def('antivirus.0.protocols_0_options', 'String');
create_var_def('antivirus.0.webhttp', 'String');
create_var_def('antivirus.0.filetransfert', 'String');
create_var_def('antivirus.0.mailsmtp', 'String');
create_var_def('antivirus.0.mailpop3', 'String');
create_var_def('antivirus.0.mailimap', 'String');
create_var_def('antivirus.0.mailmapi', 'String');
create_var_def('antivirus.0.newsnntp', 'String');
create_var_def('antivirus.0.comment', 'String');

}

check_mandatory_param('device_id');

$device_id = $context['device_id'];
$prefix = substr($device_id, 0, 3);
$device_id = str_replace($prefix, '', $device_id);

foreach ($context['antivirus'] as $key => $value) {
   $object_parameters['antivirus'][$value['object_id']] = $value;
}


$response = execute_command_and_verify_response($device_id, "UPDATE", $object_parameters, "UPDATE antivirus");
  $response = json_decode($response, true);
if ($response['wo_status'] !== ENDED) {
	$response = prepare_json_response($response['wo_status'], $response['wo_comment'], $context, true);
	echo $response;
	exit;
}

$response = prepare_json_response(ENDED, "order command execute successfull", $response['wo_newparams'], true);
echo $response;
?>
