<?php

/**
 * This file is necessary to include to use all the in-built libraries of /opt/fmc_repository/Reference/Common
 */
require_once '/opt/fmc_repository/Process/Reference/Common/common.php';

/**
 * List all the parameters required by the task
 */
function list_args()
{
}

$var = get_vars_value('UBI_SMTP_IPADDR');
/**
 * End of the task (choose one)
 */
task_success('Task OK ' . $var);
task_error('Task FAILED');
?>