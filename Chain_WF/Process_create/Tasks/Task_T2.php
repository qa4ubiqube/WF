<?php

/**
 * This file is necessary to include to use all the in-built libraries of /opt/fmc_repository/Reference/Common
 */
require_once '/opt/fmc_repository/Process/Reference/Common/common.php';
$ret = prepare_json_response(ENDED, 'Task Failed', $context, true);
sleep(60);
echo "$ret\n";
exit;
