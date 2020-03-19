#!/bin/bash

GR_PY_PATH=/usr/lib/python2.7/dist-packages/
REPO_PATH=/home/siplab/proj/dsp_ws/dsp/

export PYTHONPATH=$GR_PY_PATH
export PYTHONPATH=$PYTHONPATH:$REPO_PATH/vendor/red-pitaya-notes/projects/sdr_transceiver/gnuradio/
export PYTHONPATH=$PYTHONPATH:$REPO_PATH/vendor/red-pitaya-notes/projects/sdr_transceiver_wide/gnuradio/
export PYTHONPATH=$PYTHONPATH:/usr/local/lib/python3/dist-packages/
export GRC_BLOCKS_PATH=$REPO_PATH/vendor/red-pitaya-notes/
