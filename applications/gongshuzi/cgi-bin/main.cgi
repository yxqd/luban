#!/usr/bin/env sh

export EXPORT_ROOT=/home/linjiao/dv/tools/pythia-0.8
export PYTHONPATH=$EXPORT_ROOT/modules:$PYTHONPATH
export PATH=$EXPORT_ROOT/bin:$PATH
webmain.py $@
