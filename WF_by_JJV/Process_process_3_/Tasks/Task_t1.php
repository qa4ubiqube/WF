<?php

require_once '/opt/fmc_repository/Process/Reference/Common/common.php';
//111111111111111111111111111111111111111111

function list_args()
{
  create_var_def('sleep', 'Integer');

  
}

sleep($context['sleep']);
task_success('Task OK');
?>