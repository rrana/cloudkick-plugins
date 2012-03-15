#!/bin/bash

# Name of the process to be monitored
PROCESS_NAME="mongod"

NUM_PROCESSES=`ps ax | grep "$PROCESS_NAME" | grep -v grep | wc -l`

if [ "$NUM_PROCESSES" -lt "1" ]; then
  echo "status err $PROCESS_NAME is not running"
else
  echo "status ok $PROCESS_NAME is running"
fi
