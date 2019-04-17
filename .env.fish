#!/usr/local/bin/fish


set -gx PYTHONPATH "/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages"
set -gx PYTHONPATH (pwd)"/vendor/red-pitaya-notes/projects/sdr_transceiver/gnuradio/:""$PYTHONPATH"
set -gx PYTHONPATH (pwd)"/vendor/red-pitaya-notes/projects/sdr_transceiver_wide/gnuradio/:""$PYTHONPATH"
set -gx GRC_BLOCKS_PATH (pwd)"/vendor/red-pitaya-notes/"