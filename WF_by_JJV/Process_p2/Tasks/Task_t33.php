<?php
//23333333333333333333333333
require_once '/opt/fmc_repository/Process/Reference/Common/common.php';

function list_args()
{
  create_var_def('sleep', 'Integer');

  
}

sleep($context['sleep']);
task_success('Task OK');
?>