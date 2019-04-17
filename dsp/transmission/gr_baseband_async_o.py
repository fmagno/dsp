#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Baseband Async O
# Generated: Tue Apr 16 11:20:50 2019
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


class gr_baseband_async_o(gr.top_block):

    def __init__(self, ch_port=1, tx_ip='192.168.5.100', samp_rate=250000, sig_in='./in.dat'):
        gr.top_block.__init__(self, "Gr Baseband Async O")

        ##################################################
        # Parameters
        ##################################################
        self.ch_port = ch_port
        self.tx_ip = tx_ip
        self.samp_rate = samp_rate
        self.sig_in = sig_in

        ##################################################
        # Blocks
        ##################################################
        self.red_pitaya_sink_0 = red_pitaya.sink(
                addr=tx_ip,
                port=1000 + ch_port,
                freq=0,
                rate=samp_rate,
                corr=0,
                ptt=True
        )

        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, 50000000)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, sig_in, False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_head_0, 0), (self.red_pitaya_sink_0, 0))

    def get_ch_port(self):
        return self.ch_port

    def set_ch_port(self, ch_port):
        self.ch_port = ch_port

    def get_tx_ip(self):
        return self.tx_ip

    def set_tx_ip(self, tx_ip):
        self.tx_ip = tx_ip

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.red_pitaya_sink_0.set_rate(self.samp_rate)

    def get_sig_in(self):
        return self.sig_in

    def set_sig_in(self, sig_in):
        self.sig_in = sig_in
        self.blocks_file_source_0.open(self.sig_in, False)


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-p", "--ch-port", dest="ch_port", type="intx", default=1,
        help="Set ch_port [default=%default]")
    parser.add_option(
        "-w", "--tx-ip", dest="tx_ip", type="string", default='192.168.5.100',
        help="Set tx ip [default=%default]")
    parser.add_option(
        "-r", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(250000),
        help="Set sample rate [default=%default]")
    parser.add_option(
        "-i", "--sig-in", dest="sig_in", type="string", default='./in.dat',
        help="Set signal in [default=%default]")
    return parser


def main(top_block_cls=gr_baseband_async_o, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(ch_port=options.ch_port, tx_ip=options.tx_ip, samp_rate=options.samp_rate, sig_in=options.sig_in)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
