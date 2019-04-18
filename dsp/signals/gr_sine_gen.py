#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Sine Gen
# Generated: Thu Apr 18 11:44:01 2019
# GNU Radio version: 3.7.12.0
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class gr_sine_gen(gr.top_block):

    def __init__(self, dir_name="./", ncycles=10, npulses=10, post_padding=0, pre_padding=0, prefix='', pwm_freq=100., samp_rate=250000, sig_amp=1, sig_freq=10000):
        gr.top_block.__init__(self, "Gr Sine Gen")

        ##################################################
        # Parameters
        ##################################################
        self.dir_name = dir_name
        self.ncycles = ncycles
        self.npulses = npulses
        self.post_padding = post_padding
        self.pre_padding = pre_padding
        self.prefix = prefix
        self.pwm_freq = pwm_freq
        self.samp_rate = samp_rate
        self.sig_amp = sig_amp
        self.sig_freq = sig_freq

        ##################################################
        # Variables
        ##################################################
        self.sig_samples = sig_samples = int(samp_rate/pwm_freq)
        self.sig_on_samples = sig_on_samples = int(samp_rate*ncycles/sig_freq)
        self.base_name = base_name = prefix + "r" + str(samp_rate).zfill(6) + "_f" + str(sig_freq).zfill(8) + "_d" + str(pre_padding) + "_g" + str(post_padding) + "_a" + str(sig_amp) + "_n" + str(ncycles).zfill(3) + "_u" + str(npulses) + "_p" + str(pwm_freq) + ".dat"
        self.total_time = total_time = float(sig_samples)/samp_rate
        self.sig_off_samples = sig_off_samples = sig_samples-sig_on_samples
        self.duty_cycle = duty_cycle = float(sig_on_samples)/sig_samples
        self.absolute_path = absolute_path = dir_name + "/" + base_name

        ##################################################
        # Blocks
        ##################################################
        self.blocks_vector_source_x_1 = blocks.vector_source_f([0]*pre_padding + ([1]*sig_on_samples + [0]*sig_off_samples)*npulses + [0]*post_padding, False, 1, [])
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, absolute_path, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, sig_freq, sig_amp, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_vector_source_x_1, 0), (self.blocks_multiply_xx_0, 1))

    def get_dir_name(self):
        return self.dir_name

    def set_dir_name(self, dir_name):
        self.dir_name = dir_name
        self.set_absolute_path(self.dir_name + "/" + self.base_name)

    def get_ncycles(self):
        return self.ncycles

    def set_ncycles(self, ncycles):
        self.ncycles = ncycles
        self.set_sig_on_samples(int(self.samp_rate*self.ncycles/self.sig_freq))
        self.set_base_name(self.prefix + "r" + str(self.samp_rate).zfill(6) + "_f" + str(self.sig_freq).zfill(8) + "_d" + str(self.pre_padding) + "_g" + str(self.post_padding) + "_a" + str(self.sig_amp) + "_n" + str(self.ncycles).zfill(3) + "_u" + str(self.npulses) + "_p" + str(self.pwm_freq) + ".dat")

    def get_npulses(self):
        return self.npulses

    def set_npulses(self, npulses):
        self.npulses = npulses
        self.blocks_vector_source_x_1.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])
        self.set_base_name(self.prefix + "r" + str(self.samp_rate).zfill(6) + "_f" + str(self.sig_freq).zfill(8) + "_d" + str(self.pre_padding) + "_g" + str(self.post_padding) + "_a" + str(self.sig_amp) + "_n" + str(self.ncycles).zfill(3) + "_u" + str(self.npulses) + "_p" + str(self.pwm_freq) + ".dat")

    def get_post_padding(self):
        return self.post_padding

    def set_post_padding(self, post_padding):
        self.post_padding = post_padding
        self.blocks_vector_source_x_1.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])
        self.set_base_name(self.prefix + "r" + str(self.samp_rate).zfill(6) + "_f" + str(self.sig_freq).zfill(8) + "_d" + str(self.pre_padding) + "_g" + str(self.post_padding) + "_a" + str(self.sig_amp) + "_n" + str(self.ncycles).zfill(3) + "_u" + str(self.npulses) + "_p" + str(self.pwm_freq) + ".dat")

    def get_pre_padding(self):
        return self.pre_padding

    def set_pre_padding(self, pre_padding):
        self.pre_padding = pre_padding
        self.blocks_vector_source_x_1.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])
        self.set_base_name(self.prefix + "r" + str(self.samp_rate).zfill(6) + "_f" + str(self.sig_freq).zfill(8) + "_d" + str(self.pre_padding) + "_g" + str(self.post_padding) + "_a" + str(self.sig_amp) + "_n" + str(self.ncycles).zfill(3) + "_u" + str(self.npulses) + "_p" + str(self.pwm_freq) + ".dat")

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_base_name(self.prefix + "r" + str(self.samp_rate).zfill(6) + "_f" + str(self.sig_freq).zfill(8) + "_d" + str(self.pre_padding) + "_g" + str(self.post_padding) + "_a" + str(self.sig_amp) + "_n" + str(self.ncycles).zfill(3) + "_u" + str(self.npulses) + "_p" + str(self.pwm_freq) + ".dat")

    def get_pwm_freq(self):
        return self.pwm_freq

    def set_pwm_freq(self, pwm_freq):
        self.pwm_freq = pwm_freq
        self.set_sig_samples(int(self.samp_rate/self.pwm_freq))
        self.set_base_name(self.prefix + "r" + str(self.samp_rate).zfill(6) + "_f" + str(self.sig_freq).zfill(8) + "_d" + str(self.pre_padding) + "_g" + str(self.post_padding) + "_a" + str(self.sig_amp) + "_n" + str(self.ncycles).zfill(3) + "_u" + str(self.npulses) + "_p" + str(self.pwm_freq) + ".dat")

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sig_on_samples(int(self.samp_rate*self.ncycles/self.sig_freq))
        self.set_total_time(float(self.sig_samples)/self.samp_rate)
        self.set_sig_samples(int(self.samp_rate/self.pwm_freq))
        self.set_base_name(self.prefix + "r" + str(self.samp_rate).zfill(6) + "_f" + str(self.sig_freq).zfill(8) + "_d" + str(self.pre_padding) + "_g" + str(self.post_padding) + "_a" + str(self.sig_amp) + "_n" + str(self.ncycles).zfill(3) + "_u" + str(self.npulses) + "_p" + str(self.pwm_freq) + ".dat")
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_sig_amp(self):
        return self.sig_amp

    def set_sig_amp(self, sig_amp):
        self.sig_amp = sig_amp
        self.set_base_name(self.prefix + "r" + str(self.samp_rate).zfill(6) + "_f" + str(self.sig_freq).zfill(8) + "_d" + str(self.pre_padding) + "_g" + str(self.post_padding) + "_a" + str(self.sig_amp) + "_n" + str(self.ncycles).zfill(3) + "_u" + str(self.npulses) + "_p" + str(self.pwm_freq) + ".dat")
        self.analog_sig_source_x_0.set_amplitude(self.sig_amp)

    def get_sig_freq(self):
        return self.sig_freq

    def set_sig_freq(self, sig_freq):
        self.sig_freq = sig_freq
        self.set_sig_on_samples(int(self.samp_rate*self.ncycles/self.sig_freq))
        self.set_base_name(self.prefix + "r" + str(self.samp_rate).zfill(6) + "_f" + str(self.sig_freq).zfill(8) + "_d" + str(self.pre_padding) + "_g" + str(self.post_padding) + "_a" + str(self.sig_amp) + "_n" + str(self.ncycles).zfill(3) + "_u" + str(self.npulses) + "_p" + str(self.pwm_freq) + ".dat")
        self.analog_sig_source_x_0.set_frequency(self.sig_freq)

    def get_sig_samples(self):
        return self.sig_samples

    def set_sig_samples(self, sig_samples):
        self.sig_samples = sig_samples
        self.set_sig_off_samples(self.sig_samples-self.sig_on_samples)
        self.set_total_time(float(self.sig_samples)/self.samp_rate)
        self.set_duty_cycle(float(self.sig_on_samples)/self.sig_samples)

    def get_sig_on_samples(self):
        return self.sig_on_samples

    def set_sig_on_samples(self, sig_on_samples):
        self.sig_on_samples = sig_on_samples
        self.set_sig_off_samples(self.sig_samples-self.sig_on_samples)
        self.set_duty_cycle(float(self.sig_on_samples)/self.sig_samples)
        self.blocks_vector_source_x_1.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])

    def get_base_name(self):
        return self.base_name

    def set_base_name(self, base_name):
        self.base_name = base_name
        self.set_absolute_path(self.dir_name + "/" + self.base_name)

    def get_total_time(self):
        return self.total_time

    def set_total_time(self, total_time):
        self.total_time = total_time

    def get_sig_off_samples(self):
        return self.sig_off_samples

    def set_sig_off_samples(self, sig_off_samples):
        self.sig_off_samples = sig_off_samples
        self.blocks_vector_source_x_1.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])

    def get_duty_cycle(self):
        return self.duty_cycle

    def set_duty_cycle(self, duty_cycle):
        self.duty_cycle = duty_cycle

    def get_absolute_path(self):
        return self.absolute_path

    def set_absolute_path(self, absolute_path):
        self.absolute_path = absolute_path
        self.blocks_file_sink_0.open(self.absolute_path)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-o", "--dir-name", dest="dir_name", type="string", default="./",
        help="Set dir name [default=%default]")
    parser.add_option(
        "-n", "--ncycles", dest="ncycles", type="intx", default=10,
        help="Set number of cycles in a pulse [default=%default]")
    parser.add_option(
        "-u", "--npulses", dest="npulses", type="intx", default=10,
        help="Set number of pulses [default=%default]")
    parser.add_option(
        "-b", "--post-padding", dest="post_padding", type="intx", default=0,
        help="Set post padding [default=%default]")
    parser.add_option(
        "-d", "--pre-padding", dest="pre_padding", type="intx", default=0,
        help="Set pre padding [default=%default]")
    parser.add_option(
        "-j", "--prefix", dest="prefix", type="string", default='',
        help="Set prefix [default=%default]")
    parser.add_option(
        "-p", "--pwm-freq", dest="pwm_freq", type="eng_float", default=eng_notation.num_to_str(100.),
        help="Set frequency of the PWM signal [default=%default]")
    parser.add_option(
        "-r", "--samp-rate", dest="samp_rate", type="intx", default=250000,
        help="Set sample rate [default=%default]")
    parser.add_option(
        "-a", "--sig-amp", dest="sig_amp", type="eng_float", default=eng_notation.num_to_str(1),
        help="Set sgnal amplitude [default=%default]")
    parser.add_option(
        "-f", "--sig-freq", dest="sig_freq", type="eng_float", default=eng_notation.num_to_str(10000),
        help="Set signal frequency [default=%default]")
    return parser


def main(top_block_cls=gr_sine_gen, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(dir_name=options.dir_name, ncycles=options.ncycles, npulses=options.npulses, post_padding=options.post_padding, pre_padding=options.pre_padding, prefix=options.prefix, pwm_freq=options.pwm_freq, samp_rate=options.samp_rate, sig_amp=options.sig_amp, sig_freq=options.sig_freq)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
