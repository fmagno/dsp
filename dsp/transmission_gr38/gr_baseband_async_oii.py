#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Baseband Async Oii
# Generated: Wed Apr 17 22:24:51 2019
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


class gr_baseband_async_oii(gr.top_block):

    def __init__(self, amplitude_calibration1=1, amplitude_calibration2=1, ch_rx1=1, ch_rx2=2, ch_tx=1, duration=250000, rx_ip1='192.168.5.100', rx_ip2='192.168.5.100', samp_rate=250000, sig_in='./in.dat', sig_out1='./out1.dat', sig_out2='./out2.dat', tx_ip='192.168.5.100'):
        gr.top_block.__init__(self, "Gr Baseband Async Oii")

        ##################################################
        # Parameters
        ##################################################
        self.amplitude_calibration1 = amplitude_calibration1
        self.amplitude_calibration2 = amplitude_calibration2
        self.ch_rx1 = ch_rx1
        self.ch_rx2 = ch_rx2
        self.ch_tx = ch_tx
        self.duration = duration
        self.rx_ip1 = rx_ip1
        self.rx_ip2 = rx_ip2
        self.samp_rate = samp_rate
        self.sig_in = sig_in
        self.sig_out1 = sig_out1
        self.sig_out2 = sig_out2
        self.tx_ip = tx_ip

        ##################################################
        # Blocks
        ##################################################
        self.red_pitaya_source_0_0 = red_pitaya.source(
                addr=rx_ip2,
                port=1000+ch_rx2,
                freq=0,
                rate=samp_rate,
                corr=0
        )

        self.red_pitaya_source_0 = red_pitaya.source(
                addr=rx_ip1,
                port=1000+ch_rx1,
                freq=0,
                rate=samp_rate,
                corr=0
        )

        self.red_pitaya_sink = red_pitaya.sink(
                addr=tx_ip,
                port=1000 + ch_tx,
                freq=0,
                rate=samp_rate,
                corr=0,
                ptt=True
        )

        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((amplitude_calibration2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((amplitude_calibration1, ))
        self.blocks_head_0_1 = blocks.head(gr.sizeof_gr_complex*1, duration)
        self.blocks_head_0_0 = blocks.head(gr.sizeof_float*1, duration)
        self.blocks_head_0 = blocks.head(gr.sizeof_float*1, duration)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, sig_in, False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, sig_out2, False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, sig_out1, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_complex_to_real_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blocks_head_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_head_0_1, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_head_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_head_0_1, 0), (self.red_pitaya_sink, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.red_pitaya_source_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.red_pitaya_source_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))

    def get_amplitude_calibration1(self):
        return self.amplitude_calibration1

    def set_amplitude_calibration1(self, amplitude_calibration1):
        self.amplitude_calibration1 = amplitude_calibration1
        self.blocks_multiply_const_vxx_0.set_k((self.amplitude_calibration1, ))

    def get_amplitude_calibration2(self):
        return self.amplitude_calibration2

    def set_amplitude_calibration2(self, amplitude_calibration2):
        self.amplitude_calibration2 = amplitude_calibration2
        self.blocks_multiply_const_vxx_0_0.set_k((self.amplitude_calibration2, ))

    def get_ch_rx1(self):
        return self.ch_rx1

    def set_ch_rx1(self, ch_rx1):
        self.ch_rx1 = ch_rx1

    def get_ch_rx2(self):
        return self.ch_rx2

    def set_ch_rx2(self, ch_rx2):
        self.ch_rx2 = ch_rx2

    def get_ch_tx(self):
        return self.ch_tx

    def set_ch_tx(self, ch_tx):
        self.ch_tx = ch_tx

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration
        self.blocks_head_0_1.set_length(self.duration)
        self.blocks_head_0_0.set_length(self.duration)
        self.blocks_head_0.set_length(self.duration)

    def get_rx_ip1(self):
        return self.rx_ip1

    def set_rx_ip1(self, rx_ip1):
        self.rx_ip1 = rx_ip1

    def get_rx_ip2(self):
        return self.rx_ip2

    def set_rx_ip2(self, rx_ip2):
        self.rx_ip2 = rx_ip2

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.red_pitaya_source_0_0.set_rate(self.samp_rate)
        self.red_pitaya_source_0.set_rate(self.samp_rate)
        self.red_pitaya_sink.set_rate(self.samp_rate)

    def get_sig_in(self):
        return self.sig_in

    def set_sig_in(self, sig_in):
        self.sig_in = sig_in
        self.blocks_file_source_0.open(self.sig_in, False)

    def get_sig_out1(self):
        return self.sig_out1

    def set_sig_out1(self, sig_out1):
        self.sig_out1 = sig_out1
        self.blocks_file_sink_0.open(self.sig_out1)

    def get_sig_out2(self):
        return self.sig_out2

    def set_sig_out2(self, sig_out2):
        self.sig_out2 = sig_out2
        self.blocks_file_sink_0_0.open(self.sig_out2)

    def get_tx_ip(self):
        return self.tx_ip

    def set_tx_ip(self, tx_ip):
        self.tx_ip = tx_ip


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-v", "--amplitude-calibration1", dest="amplitude_calibration1", type="complex", default=1,
        help="Set amplitude calibration 1 [default=%default]")
    parser.add_option(
        "-b", "--amplitude-calibration2", dest="amplitude_calibration2", type="complex", default=1,
        help="Set amplitude calibration 2 [default=%default]")
    parser.add_option(
        "-k", "--ch-rx1", dest="ch_rx1", type="intx", default=1,
        help="Set ch_rx1 [default=%default]")
    parser.add_option(
        "-y", "--ch-rx2", dest="ch_rx2", type="intx", default=2,
        help="Set ch_rx2 [default=%default]")
    parser.add_option(
        "-p", "--ch-tx", dest="ch_tx", type="intx", default=1,
        help="Set ch_tx [default=%default]")
    parser.add_option(
        "-d", "--duration", dest="duration", type="intx", default=250000,
        help="Set duration [default=%default]")
    parser.add_option(
        "-e", "--rx-ip1", dest="rx_ip1", type="string", default='192.168.5.100',
        help="Set rx ip1 [default=%default]")
    parser.add_option(
        "-t", "--rx-ip2", dest="rx_ip2", type="string", default='192.168.5.100',
        help="Set rx ip2 [default=%default]")
    parser.add_option(
        "-r", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(250000),
        help="Set sample rate [default=%default]")
    parser.add_option(
        "-i", "--sig-in", dest="sig_in", type="string", default='./in.dat',
        help="Set signal in [default=%default]")
    parser.add_option(
        "-o", "--sig-out1", dest="sig_out1", type="string", default='./out1.dat',
        help="Set signal out 1 [default=%default]")
    parser.add_option(
        "-l", "--sig-out2", dest="sig_out2", type="string", default='./out2.dat',
        help="Set signal out 2 [default=%default]")
    parser.add_option(
        "-w", "--tx-ip", dest="tx_ip", type="string", default='192.168.5.100',
        help="Set tx ip1 [default=%default]")
    return parser


def main(top_block_cls=gr_baseband_async_oii, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(amplitude_calibration1=options.amplitude_calibration1, amplitude_calibration2=options.amplitude_calibration2, ch_rx1=options.ch_rx1, ch_rx2=options.ch_rx2, ch_tx=options.ch_tx, duration=options.duration, rx_ip1=options.rx_ip1, rx_ip2=options.rx_ip2, samp_rate=options.samp_rate, sig_in=options.sig_in, sig_out1=options.sig_out1, sig_out2=options.sig_out2, tx_ip=options.tx_ip)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
