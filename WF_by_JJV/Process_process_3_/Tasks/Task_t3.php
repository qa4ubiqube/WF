<?php

require_once '/opt/fmc_repository/Process/Reference/Common/common.php';
//333333333333333333333333333333333

function list_args()
{
  create_var_def('sleep', 'Integer');

  
}

sleep($context['sleep']);
task_success('Task OK');
?>