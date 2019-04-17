#!/bin/bash

MY_PATH="`dirname \"$0\"`"              # relative
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"  # absolutized and normalized
if [ -z "$MY_PATH" ] ; then
    # error; for some reason, the path is not accessible
    # to the script (e.g. permissions re-evaled after suid)
    exit 1  # fail
fi
echo "$MY_PATH"

export PYTHONPATH=/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages
export PYTHONPATH=${PYTHONPATH}:$(MY_PATH)/vendor/red-pitaya-notes/projects/sdr_transceiver/gnuradio/
export PYTHONPATH=${PYTHONPATH}:$(MY_PATH)/vendor/red-pitaya-notes/projects/sdr_transceiver_wide/gnuradio/
export GRC_BLOCKS_PATH=$(MY_PATH)/vendor/red-pitaya-notes/