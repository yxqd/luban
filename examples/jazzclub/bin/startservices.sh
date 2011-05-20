#!/usr/bin/env bash

# this script has to be run under this directory.
# need to make sure jazzclub python package is in the path
export PYTHONPATH=..:$PYTHONPATH

#create tables
./createtable.py --name=Registrant.Registrant
./createtable.py --name=User.User
./createtable.py --name=Thread.Thread
./createtable.py --name=Message.Message

ipad.py --config=../config,/tmp/luban-services --- --home=../config
