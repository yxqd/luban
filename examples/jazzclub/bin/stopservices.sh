#!/usr/bin/env bash

# this script has to be run under this directory.
# need to make sure jazzclub python package is in the path
# export PYTHONPATH=..:$PYTHONPATH

ipad.py --config=../config,/tmp/luban-services --- -stop --home=../config
