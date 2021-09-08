<?php

require_once '/opt/fmc_repository/Process/Reference/Common/common.php';

function list_args()
{
  create_var_def('sleep', 'Integer');
  create_var_def('mydevice', 'Device');
  create_var_def('int', 'Integer');
  create_var_def('ref', 'OBMFRef');
  
}

sleep($context['sleep']);
task_success('Task OK');
?>