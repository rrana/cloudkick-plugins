#!/bin/bash

# process_count.sh <process_name>
# Cloudkick plugin to check if a named process is running and count number of
# processes. The process name is matched as regex.


if [ $# -ne 1 ]; then
  echo -e "usage: `basename $0` <process_name>"
  exit 1
fi

PS_COUNT=`ps -Ao command | grep -ve grep -e process_count.sh | grep -ce $1`

if [ "$PS_COUNT" -lt "1" ]; then
  echo "status err $1 has 0 processes"
else
  echo "status ok $1 has $PS_COUNT processes"
  echo "metric process_count_$1 int $PS_COUNT"
fi
