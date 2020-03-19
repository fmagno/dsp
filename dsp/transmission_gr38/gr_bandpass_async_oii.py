#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Gr Bandpass Async Oii
# GNU Radio version: 3.8.0.0

from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import red_pitaya

class gr_bandpass_async_oii(gr.top_block):

    def __init__(self, amplitude_calibration1=1, amplitude_calibration2=1, center_freq=0, ch_rx1=1001, ch_rx2=1002, ch_tx=1001, duration=250000, rx_ip1="192.168.5.101", rx_ip2="192.168.5.101", samp_rate=250000, sig_in="./in.dat", sig_out1="./out1.dat", sig_out2="./out2.dat", tx_ip="192.168.5.101"):
        gr.top_block.__init__(self, "Gr Bandpass Async Oii")

        ##################################################
        # Parameters
        ##################################################
        self.amplitude_calibration1 = amplitude_calibration1
        self.amplitude_calibration2 = amplitude_calibration2
        self.center_freq = center_freq
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
        self.red_pitaya_source_xx_0_0 = red_pitaya.source(addr=rx_ip2,port=ch_rx2,freq=center_freq,rate=samp_rate,corr=0)
        self.red_pitaya_source_xx_0 = red_pitaya.source(addr=rx_ip1,port=ch_rx1,freq=center_freq,rate=samp_rate,corr=0)
        self.red_pitaya_sink_xx_0 = red_pitaya.sink(addr=tx_ip,port=ch_tx,freq=center_freq,rate=samp_rate,corr=0,ptt=True)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_cc(amplitude_calibration2)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(amplitude_calibration1)
        self.blocks_head_0_1 = blocks.head(gr.sizeof_gr_complex*1, duration)
        self.blocks_head_0_0 = blocks.head(gr.sizeof_float*1, duration)
        self.blocks_head_0 = blocks.head(gr.sizeof_float*1, duration)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, sig_in, False, 0, 0)
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
        self.connect((self.blocks_head_0_1, 0), (self.red_pitaya_sink_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.red_pitaya_source_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.red_pitaya_source_xx_0_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))

    def get_amplitude_calibration1(self):
        return self.amplitude_calibration1

    def set_amplitude_calibration1(self, amplitude_calibration1):
        self.amplitude_calibration1 = amplitude_calibration1
        self.blocks_multiply_const_vxx_0.set_k(self.amplitude_calibration1)

    def get_amplitude_calibration2(self):
        return self.amplitude_calibration2

    def set_amplitude_calibration2(self, amplitude_calibration2):
        self.amplitude_calibration2 = amplitude_calibration2
        self.blocks_multiply_const_vxx_0_0.set_k(self.amplitude_calibration2)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.red_pitaya_sink_xx_0.set_freq(self.center_freq, 0)
        self.red_pitaya_source_xx_0.set_freq(self.center_freq, 0)
        self.red_pitaya_source_xx_0_0.set_freq(self.center_freq, 0)

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
        self.blocks_head_0.set_length(self.duration)
        self.blocks_head_0_0.set_length(self.duration)
        self.blocks_head_0_1.set_length(self.duration)

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
        self.red_pitaya_sink_xx_0.set_rate(self.samp_rate)
        self.red_pitaya_source_xx_0.set_rate(self.samp_rate)
        self.red_pitaya_source_xx_0_0.set_rate(self.samp_rate)

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
    parser = ArgumentParser()
    parser.add_argument(
        "-v", "--amplitude-calibration1", dest="amplitude_calibration1", type=complex, default=1,
        help="Set amplitude calibration 1 [default=%(default)r]")
    parser.add_argument(
        "-b", "--amplitude-calibration2", dest="amplitude_calibration2", type=complex, default=1,
        help="Set amplitude calibration 2 [default=%(default)r]")
    parser.add_argument(
        "-c", "--center-freq", dest="center_freq", type=eng_float, default="0.0",
        help="Set center_freq [default=%(default)r]")
    parser.add_argument(
        "-k", "--ch-rx1", dest="ch_rx1", type=intx, default=1001,
        help="Set ch_rx1 [default=%(default)r]")
    parser.add_argument(
        "-y", "--ch-rx2", dest="ch_rx2", type=intx, default=1002,
        help="Set ch_rx2 [default=%(default)r]")
    parser.add_argument(
        "-p", "--ch-tx", dest="ch_tx", type=intx, default=1001,
        help="Set ch_tx [default=%(default)r]")
    parser.add_argument(
        "-d", "--duration", dest="duration", type=intx, default=250000,
        help="Set duration [default=%(default)r]")
    parser.add_argument(
        "-r", "--samp-rate", dest="samp_rate", type=eng_float, default="250.0k",
        help="Set sample rate [default=%(default)r]")
    return parser


def main(top_block_cls=gr_bandpass_async_oii, options=None):
    if options is None:
        options = argument_parser().parse_args()
    tb = top_block_cls(amplitude_calibration1=options.amplitude_calibration1, amplitude_calibration2=options.amplitude_calibration2, center_freq=options.center_freq, ch_rx1=options.ch_rx1, ch_rx2=options.ch_rx2, ch_tx=options.ch_tx, duration=options.duration, samp_rate=options.samp_rate)

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
