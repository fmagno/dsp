#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: gr_sandbox
# Generated: Wed Jul 10 10:40:27 2019
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


class gr_sandbox(gr.top_block):

    def __init__(self, ch_port=1, duration=250000, rx_ip='192.168.5.101', samp_rate=250000, sig_in='./in.dat', sig_out='./out.dat', tx_ip='192.168.5.101'):
        gr.top_block.__init__(self, "gr_sandbox")

        ##################################################
        # Parameters
        ##################################################
        self.ch_port = ch_port
        self.duration = duration
        self.rx_ip = rx_ip
        self.samp_rate = samp_rate
        self.sig_in = sig_in
        self.sig_out = sig_out
        self.tx_ip = tx_ip

        ##################################################
        # Blocks
        ##################################################
        self.red_pitaya_source_0 = red_pitaya.source(
                addr=rx_ip,
                port=1000+ch_port,
                freq=0,
                rate=samp_rate,
                corr=0
        )

        self.red_pitaya_sink_0 = red_pitaya.sink(
                addr=tx_ip,
                port=1000 + ch_port,
                freq=0,
                rate=samp_rate,
                corr=0,
                ptt=True
        )

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
        self.connect((self.blocks_float_to_complex_0, 0), (self.red_pitaya_sink_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.red_pitaya_source_0, 0), (self.blocks_complex_to_real_0, 0))

    def get_ch_port(self):
        return self.ch_port

    def set_ch_port(self, ch_port):
        self.ch_port = ch_port

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration
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
        self.red_pitaya_sink_0.set_rate(self.samp_rate)

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


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "-p", "--ch-port", dest="ch_port", type="intx", default=1,
        help="Set ch_port [default=%default]")
    parser.add_option(
        "-d", "--duration", dest="duration", type="long", default=250000,
        help="Set duration [default=%default]")
    parser.add_option(
        "-e", "--rx-ip", dest="rx_ip", type="string", default='192.168.5.101',
        help="Set rx ip [default=%default]")
    parser.add_option(
        "-r", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(250000),
        help="Set sample rate [default=%default]")
    parser.add_option(
        "-i", "--sig-in", dest="sig_in", type="string", default='./in.dat',
        help="Set signal in [default=%default]")
    parser.add_option(
        "-o", "--sig-out", dest="sig_out", type="string", default='./out.dat',
        help="Set signal out [default=%default]")
    parser.add_option(
        "-w", "--tx-ip", dest="tx_ip", type="string", default='192.168.5.101',
        help="Set tx ip [default=%default]")
    return parser


def main(top_block_cls=gr_sandbox, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    tb = top_block_cls(ch_port=options.ch_port, duration=options.duration, rx_ip=options.rx_ip, samp_rate=options.samp_rate, sig_in=options.sig_in, sig_out=options.sig_out, tx_ip=options.tx_ip)
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
