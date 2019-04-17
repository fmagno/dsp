import toml
import datetime
import numpy as np

from dsp.signals.gr_sine_gen import gr_sine_gen


def gen_sine(*args, **kwargs):
    """ Generates sine_gen signals for a specific frequency
    of an experiment"""
    exp = kwargs['exp']
    exp_signals = exp['signals']
    exp_abspath = kwargs['exp_abspath']
    status_abspath = kwargs['status_abspath']
    date = kwargs['exp_date']

    if 'sig_freq' in exp_signals:
        desired_freqs = [exp_signals['sig_freq']]
    else:
        desired_freqs = np.arange(
            exp['first_freq'],
            exp['last_freq'] + exp['freq_step'],
            exp['freq_step']
        )
    desired_freqs = map(str, desired_freqs)

    # Check if signals are already created
    with open(status_abspath, 'r') as fd:
        status = toml.loads(fd.read())

    done_freqs = status['done_freqs']

    # Determine the difference between the desired freqs and
    # the ones that have already been done
    diff_freqs = list(sorted(set(desired_freqs).difference(done_freqs)))

    # Generate signals and update STATUS file
    if diff_freqs:
        with open(status_abspath, 'w+') as fd:
            for freq in diff_freqs:
                # Generate signal
                gr_run = gr_sine_gen(
                    dir_name=str(exp_abspath),
                    ncycles=exp_signals['ncycles'],
                    npulses=exp_signals['npulses'],
                    pre_padding=exp_signals['pre_padding'],
                    post_padding=exp_signals['post_padding'],
                    prefix='i' + date + '_',
                    pwm_freq=exp_signals['pwm_freq'],
                    samp_rate=exp_signals['samp_rate'],
                    sig_amp=exp_signals['sig_amp'],
                    sig_freq=float(freq),
                )
                gr_run.start()
                gr_run.wait()

                # Update status
                status['done_freqs'] = sorted(status['done_freqs'] + [str(freq).zfill(8)])
                fd.seek(0)
                fd.write(toml.dumps(status))
                fd.truncate()

    print('Signals generated!!!')


def generate_signals(*args, **kwargs):
    if kwargs['exp']['signals']['type'] == 'gr_sine_gen':
        gen_sine(*args, **kwargs)
    else:
        raise


