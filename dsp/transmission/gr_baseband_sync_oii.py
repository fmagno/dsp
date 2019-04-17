#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Baseband Sync Oii
# Generated: Tue Apr 16 12:11:08 2019
# GNU Radio version: 3.7.12.0
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import red_pitaya_wide


class gr_baseband_sync_oii(gr.top_block):

    def __init__(self, amplitude_calibration=3.7929649, duration=250000, rx_ip='192.168.5.100', samp_rate=250000, sig_in="./in.dat", sig_out_ch1="./r250000_ch1.dat", sig_out_ch2="./r250000_ch2.dat", tx_ip='192.168.5.100'):
        gr.top_block.__init__(self, "Gr Baseband Sync Oii")

        ##################################################
        # Parameters
        ##################################################
        self.amplitude_calibration = amplitude_calibration
        self.duration = duration
        self.rx_ip = rx_ip
        self.samp_rate = samp_rate
        self.sig_in = sig_in
        self.sig_out_ch1 = sig_out_ch1
        self.sig_out_ch2 = sig_out_ch2
        self.tx_ip = tx_ip

        ##################################################
        # Variables
        ##################################################
        self.freq_correction = freq_correction = 0
        self.center_freq = center_freq = 0

        ##################################################
        # Blocks
        ##################################################
        self.red_pitaya_wide_source_0 = red_pitaya_wide.source(
                addr=rx_ip,
                port=1001,
                freq=center_freq,
                rate=samp_rate,
                mask=3,
                corr=0
        )

        self.red_pitaya_wide_sink_0 = red_pitaya_wide.sink(
                addr=tx_ip,
                port=1001,
                freq=center_freq,
                rate=samp_rate,
                mask=3,
                corr=0,
                ptt=True
        )

        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((amplitude_calibration, ))
        self.blocks_head_0_0_1 = blocks.head(gr.sizeof_gr_complex*1, duration)
        self.blocks_head_0_0 = blocks.head(gr.sizeof_gr_complex*1, duration)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, sig_in, False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, sig_out_ch2, False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, sig_out_ch1, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_head_0_0_1, 0))
        self.connect((self.blocks_head_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_head_0_0_1, 0), (self.red_pitaya_wide_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.red_pitaya_wide_source_0, 0), (self.blocks_head_0_0, 0))

    def get_amplitude_calibration(self):
        return self.amplitude_calibration

    def set_amplitude_calibration(self, amplitude_calibration):
        self.amplitude_calibration = amplitude_calibration
        self.blocks_multiply_const_vxx_0.set_k((self.amplitude_calibration, ))

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration
        self.blocks_head_0_0_1.set_length(self.duration)
        self.blocks_head_0_0.set_length(self.duration)

    def get_rx_ip(self):
        return self.rx_ip

    def set_rx_ip(self, rx_ip):
        self.rx_ip = rx_ip

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.red_pitaya_wide_source_0.set_rate(self.samp_rate)
        self.red_pitaya_wide_sink_0.set_rate(self.samp_rate)

    def get_sig_in(self):
        return self.sig_in

    def set_sig_in(self, sig_in):
        self.sig_in = sig_in
        self.blocks_file_source_0.open(self.sig_in, False)

    def get_sig_out_ch1(self):
        return self.sig_out_ch1

    def set_sig_out_ch1(self, sig_out_ch1):
        self.sig_out_ch1 = sig_out_ch1
        self.blocks_file_sink_0.open(self.sig_out_ch1)

    def get_sig_out_ch2(self):
        return self.sig_out_ch2

    def set_sig_out_ch2(self, sig_out_ch2):
        self.sig_out_ch2 = sig_out_ch2
        self.blocks_file_sink_0_0.open(self.sig_out_ch2)

    def get_tx_ip(self):
        return self.tx_ip

    def set_tx_ip(self, tx_ip):
        self.tx_ip = tx_ip

    def get_freq_correction(self):
        return self.freq_correction

    def set_freq_correction(self, freq_correction):
        self.freq_correction = freq_correction

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.red_pitaya_wide_source_0.set_freq(self.center_freq, 0)
        self.red_pitaya_wide_sink_0.set_freq(self.center_freq, 0)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-y", "--amplitude-calibration", dest="amplitude_calibration", type="eng_float", default=eng_notation.num_to_str(3.7929649),
        help="Set amplitude calibration factor [default=%default]")
    parser.add_option(
        "-d", "--duration", dest="duration", type="intx", default=250000,
        help="Set duration [default=%default]")
    parser.add_option(
        "-w", "--rx-ip", dest="rx_ip", type="string", default='192.168.5.100',
        help="Set rp reception ip [default=%default]")
    parser.add_option(
        "-r", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(250000),
        help="Set sample rate [default=%default]")
    parser.add_option(
        "-i", "--sig-in", dest="sig_in", type="string", default="./in.dat",
        help="Set signal in [default=%default]")
    parser.add_option(
        "-o", "--sig-out-ch1", dest="sig_out_ch1", type="string", default="./r250000_ch1.dat",
        help="Set signal output channel 1 [default=%default]")
    parser.add_option(
        "-l", "--sig-out-ch2", dest="sig_out_ch2", type="string", default="./r250000_ch2.dat",
        help="Set signal output channel 2 [default=%default]")
    parser.add_option(
        "-t", "--tx-ip", dest="tx_ip", type="string", default='192.168.5.100',
        help="Set rp transmission ip [default=%default]")
    return parser


def main(top_block_cls=gr_baseband_sync_oii, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(amplitude_calibration=options.amplitude_calibration, duration=options.duration, rx_ip=options.rx_ip, samp_rate=options.samp_rate, sig_in=options.sig_in, sig_out_ch1=options.sig_out_ch1, sig_out_ch2=options.sig_out_ch2, tx_ip=options.tx_ip)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
