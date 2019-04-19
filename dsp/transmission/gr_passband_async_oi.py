#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Passband Async Oi
# Generated: Fri Apr 19 12:23:43 2019
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
import red_pitaya


class gr_passband_async_oi(gr.top_block):

    def __init__(self, amplitude_calibration=1, ch_rx=1, ch_tx=1, duration=250000, rx_ip='192.168.5.100', samp_rate=250000, sig_in='./in.dat', sig_out='./out1.dat', tx_ip='192.168.5.100', center_freq=50000):
        gr.top_block.__init__(self, "Gr Passband Async Oi")

        ##################################################
        # Parameters
        ##################################################
        self.amplitude_calibration = amplitude_calibration
        self.ch_rx = ch_rx
        self.ch_tx = ch_tx
        self.duration = duration
        self.rx_ip = rx_ip
        self.samp_rate = samp_rate
        self.sig_in = sig_in
        self.sig_out = sig_out
        self.tx_ip = tx_ip
        self.center_freq = center_freq

        ##################################################
        # Blocks
        ##################################################
        self.red_pitaya_source_0 = red_pitaya.source(
                addr=rx_ip,
                port=1000+ch_rx,
                freq=center_freq,
                rate=samp_rate,
                corr=0
        )

        self.red_pitaya_sink = red_pitaya.sink(
                addr=tx_ip,
                port=1000 + ch_tx,
                freq=center_freq,
                rate=samp_rate,
                corr=0,
                ptt=True
        )

        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((amplitude_calibration, ))
        self.blocks_head_0_1 = blocks.head(gr.sizeof_gr_complex*1, duration)
        self.blocks_head_0 = blocks.head(gr.sizeof_float*1, duration)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, sig_in, False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, sig_out, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_head_0_1, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_head_0_1, 0), (self.red_pitaya_sink, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.red_pitaya_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def get_amplitude_calibration(self):
        return self.amplitude_calibration

    def set_amplitude_calibration(self, amplitude_calibration):
        self.amplitude_calibration = amplitude_calibration
        self.blocks_multiply_const_vxx_0.set_k((self.amplitude_calibration, ))

    def get_ch_rx(self):
        return self.ch_rx

    def set_ch_rx(self, ch_rx):
        self.ch_rx = ch_rx

    def get_ch_tx(self):
        return self.ch_tx

    def set_ch_tx(self, ch_tx):
        self.ch_tx = ch_tx

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration
        self.blocks_head_0_1.set_length(self.duration)
        self.blocks_head_0.set_length(self.duration)

    def get_rx_ip(self):
        return self.rx_ip

    def set_rx_ip(self, rx_ip):
        self.rx_ip = rx_ip

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.red_pitaya_source_0.set_rate(self.samp_rate)
        self.red_pitaya_sink.set_rate(self.samp_rate)

    def get_sig_in(self):
        return self.sig_in

    def set_sig_in(self, sig_in):
        self.sig_in = sig_in
        self.blocks_file_source_0.open(self.sig_in, False)

    def get_sig_out(self):
        return self.sig_out

    def set_sig_out(self, sig_out):
        self.sig_out = sig_out
        self.blocks_file_sink_0.open(self.sig_out)

    def get_tx_ip(self):
        return self.tx_ip

    def set_tx_ip(self, tx_ip):
        self.tx_ip = tx_ip

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.red_pitaya_source_0.set_freq(self.center_freq, 0)
        self.red_pitaya_sink.set_freq(self.center_freq, 0)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-v", "--amplitude-calibration", dest="amplitude_calibration", type="complex", default=1,
        help="Set amplitude calibration  [default=%default]")
    parser.add_option(
        "-k", "--ch-rx", dest="ch_rx", type="intx", default=1,
        help="Set ch_rx [default=%default]")
    parser.add_option(
        "-p", "--ch-tx", dest="ch_tx", type="intx", default=1,
        help="Set ch_tx [default=%default]")
    parser.add_option(
        "-d", "--duration", dest="duration", type="intx", default=250000,
        help="Set duration [default=%default]")
    parser.add_option(
        "-e", "--rx-ip", dest="rx_ip", type="string", default='192.168.5.100',
        help="Set rx ip [default=%default]")
    parser.add_option(
        "-r", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(250000),
        help="Set sample rate [default=%default]")
    parser.add_option(
        "-i", "--sig-in", dest="sig_in", type="string", default='./in.dat',
        help="Set signal in [default=%default]")
    parser.add_option(
        "-o", "--sig-out", dest="sig_out", type="string", default='./out1.dat',
        help="Set signal out [default=%default]")
    parser.add_option(
        "-w", "--tx-ip", dest="tx_ip", type="string", default='192.168.5.100',
        help="Set tx ip [default=%default]")
    parser.add_option(
        "-g", "--center-freq", dest="center_freq", type="eng_float", default=eng_notation.num_to_str(50000),
        help="Set center frequency [default=%default]")
    return parser


def main(top_block_cls=gr_passband_async_oi, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(amplitude_calibration=options.amplitude_calibration, ch_rx=options.ch_rx, ch_tx=options.ch_tx, duration=options.duration, rx_ip=options.rx_ip, samp_rate=options.samp_rate, sig_in=options.sig_in, sig_out=options.sig_out, tx_ip=options.tx_ip, center_freq=options.center_freq)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
