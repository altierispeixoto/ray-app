#!/bin/bash -xe
# @script       run.sh
# @author       Anthony Vilarim Caliani
#
# @params
# 01 - Node Type
#
# @usage
# ./run.sh [ 'head' | 'worker' ]
NODE_TYPE="${1:?'Node type not specified!'}"

if [[ "$NODE_TYPE" == "head" ]]; then
  ray start --head --port=6379 --dashboard-host=0.0.0.0
elif [ "$NODE_TYPE" == "worker" ]; then
  ray start --address=head-node:6379
else
  echo "Invalid node type '$NODE_TYPE'! Options: head, worker"
  exit 1
fi

tail -f /dev/null && exit 0
