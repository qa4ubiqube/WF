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

  create_var_def('device', 'Managed Entity');

  

}

preg_match('/(?<digit>\d+)/',$context['device'],$device_id_number);
$context['device_id_number']=$device_id_number[1];
$context['cmd']="/opt/ubi-jentreprise/bin/api/device/readDeviceById.sh ".$context['device_id_number'];
$response_cmd= shell_exec($context['cmd']);
preg_match('#<ipAddress>\n<address>(.*)</address>\n<mask>#',$response_cmd, $out);
$context['device_ip']=$out[1];

?>