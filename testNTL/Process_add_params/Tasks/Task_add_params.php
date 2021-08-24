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
  /**
   * You can use var_name convention for your variables
   * They will display automaticaly as "Var Name"
   * The allowed types are:
   *    'String', 'Boolean', 'Integer', 'Password', 'IpAddress',
   *    'IpMask', 'Ipv6Address', 'Composite', 'OBMFRef', 'Device'
   *
   * Add as many variables as needed
   */
  create_var_def('var_name', 'String');
  create_var_def('var_name2', 'Integer');
    create_var_def('var_name3', 'String');

}

/**
 * A function to check whether all the mandatory parameters are present in user-input
 *
 * The function needs to be called for each mandatory parameter.
 * This function call prevents the Task execution whenever there is a mandatory parameter missing,
 * and gives error at the beginning itself preventing any issues in-between/end of the Task due to a missing mandatory parameter.
 *
 *
 * NOTE : There might be cases where conditions are required.
 * For ex. if (empty($context['var_name']) || (empty($context['var_name2']) && empty($context['var_name3']))) => FAIL [Don't proceed]
 * Such cases need to be handled as per the Task logic
 */
check_mandatory_param('var_name');
check_mandatory_param('var_name2');
check_mandatory_param('var_name3');






/**
 * End of the task (choose one)
 */
task_success('Task OK');
task_error('Task FAILED');
?>