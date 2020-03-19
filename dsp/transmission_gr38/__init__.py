import toml
import glob
import time
import datetime
import numpy as np
import os
import time

from dsp.transmission.gr_baseband_async_oii import gr_baseband_async_oii


def baseband_async_oii(*args, **kwargs):
    """ baseband async oii"""
    exp = kwargs['exp']
    exp_transmission = exp['transmission']
    exp_abspath = kwargs['exp_abspath']
    status_abspath = kwargs['status_abspath']
    date = kwargs['exp_date']

    # Read status file
    with open(status_abspath, 'r') as fd:
        status = toml.loads(fd.read())

    desired_transmissions = status['done_freqs']
    done_transmissions = status['done_transmissions']
    diff_transmissions = list(sorted(set(desired_transmissions).difference(done_transmissions)))

    with open(status_abspath, 'w+') as fd:
        for dt in diff_transmissions:
            # import pdb; pdb.set_trace()
            sig = glob.glob(os.path.join(exp_abspath, 'i*_f{}*.dat'.format(dt)))[0]
            for sample in range(exp['samples']):
                gr_run = gr_baseband_async_oii(
                    sig_in=str(sig),
                    sig_out1=str(os.path.join(exp_abspath, 'o'+date+'_f'+dt+'s'+str(sample) + 'ch1' + '.dat')),
                    sig_out2=str(os.path.join(exp_abspath, 'o'+date+'_f'+dt+'s'+str(sample) + 'ch2' + '.dat')),
                    samp_rate=exp_transmission['samp_rate'],
                    tx_ip=str(exp_transmission['tx_ip']),
                    rx_ip1=str(exp_transmission['rx_ip1']),
                    rx_ip2=str(exp_transmission['rx_ip2']),
                    ch_tx=exp_transmission['ch_tx'],
                    ch_rx1=exp_transmission['ch_rx1'],
                    ch_rx2=exp_transmission['ch_rx2'],
                    duration=exp_transmission['duration'],
                    amplitude_calibration1=exp_transmission['amplitude_calibration1'],
                    amplitude_calibration2=exp_transmission['amplitude_calibration2'],
                )
                print('Running...')
                # import pdb; pdb.set_trace()
                gr_run.start()
                time.sleep(1)
                gr_run.wait()
                time.sleep(1)

                # Update status
                status['done_transmissions'] = sorted(status['done_transmissions'] + [str(dt).zfill(8)])
                fd.seek(0)
                fd.write(toml.dumps(status))
                fd.truncate()



def begin_transmission(*args, **kwargs):
    if kwargs['exp']['transmission']['type'] == 'gr_baseband_async_oii':
        baseband_async_oii(*args, **kwargs)
    else:
        raise
