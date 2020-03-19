#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Gr Chirp F
# Generated: Wed May  8 15:24:17 2019
##################################################


from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser


class gr_chirp_f(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Gr Chirp F")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 250000
        self.pi_val = pi_val = 3.14159265359
        self.freq = freq = 115000
        self.sig_on_samples = sig_on_samples = samp_rate
        self.sig_off_samples = sig_off_samples = samp_rate
        self.sens = sens = 2*pi_val*freq
        self.pre_padding = pre_padding = samp_rate
        self.post_padding = post_padding = 0
        self.npulses = npulses = 2

        ##################################################
        # Blocks
        ##################################################
        self.blocks_vector_source_x_0 = blocks.vector_source_f([0]*pre_padding + ([1]*sig_on_samples + [0]*sig_off_samples)*npulses + [0]*post_padding, False, 1, [])
        self.blocks_vco_f_0 = blocks.vco_f(samp_rate, sens, 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, '/home/siplab/proj/dsp_ws/cpn_faro/tekever/signals/chirp/chirp.dat', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, samp_rate/2)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, 1, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_vco_f_0, 0))
        self.connect((self.blocks_vco_f_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_xx_0, 1))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sig_on_samples(self.samp_rate)
        self.set_sig_off_samples(self.samp_rate)
        self.set_pre_padding(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_delay_0.set_dly(self.samp_rate/2)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_pi_val(self):
        return self.pi_val

    def set_pi_val(self, pi_val):
        self.pi_val = pi_val
        self.set_sens(2*self.pi_val*self.freq)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_sens(2*self.pi_val*self.freq)

    def get_sig_on_samples(self):
        return self.sig_on_samples

    def set_sig_on_samples(self, sig_on_samples):
        self.sig_on_samples = sig_on_samples
        self.blocks_vector_source_x_0.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])

    def get_sig_off_samples(self):
        return self.sig_off_samples

    def set_sig_off_samples(self, sig_off_samples):
        self.sig_off_samples = sig_off_samples
        self.blocks_vector_source_x_0.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])

    def get_sens(self):
        return self.sens

    def set_sens(self, sens):
        self.sens = sens

    def get_pre_padding(self):
        return self.pre_padding

    def set_pre_padding(self, pre_padding):
        self.pre_padding = pre_padding
        self.blocks_vector_source_x_0.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])

    def get_post_padding(self):
        return self.post_padding

    def set_post_padding(self, post_padding):
        self.post_padding = post_padding
        self.blocks_vector_source_x_0.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])

    def get_npulses(self):
        return self.npulses

    def set_npulses(self, npulses):
        self.npulses = npulses
        self.blocks_vector_source_x_0.set_data([0]*self.pre_padding + ([1]*self.sig_on_samples + [0]*self.sig_off_samples)*self.npulses + [0]*self.post_padding, [])


def main(top_block_cls=gr_chirp_f, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
