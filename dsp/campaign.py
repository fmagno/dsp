#!/usr/bin/env python
""" """
import os
import toml
import time
import datetime
import numpy as np

from dsp import tools
from dsp.signals import generate_signals
from dsp.transmission import begin_transmission




class Campaign(object):
    """ Campaign"""
    data = None
    abspath = None
    active_exp = None
    active_exp_abspath = None
    create_date = None
    status_abspath = None


    def __init__(self, config_path='./config.ini'):
        """ Load the campaign config file onto structured data in memory
        and create campaign folder if it does not already exist"""
        with open(config_path, 'r') as fd:
            self.data = toml.loads(fd.read())

        self.abspath = os.path.abspath(os.path.join(self.data['campaign']['dir'], self.data['campaign']['name']))
        tools.mkdir_p(self.abspath)

        # store .ini
        self.date = str(datetime.datetime.now()).split('.')[0].replace(' ', '_')
        with open(os.path.join(self.abspath, self.date + '_' + self.data['campaign']['name']) + '.ini', 'w+') as fd:
            fd.write(toml.dumps(self.data))

    def activate_experiment(self, exp):
        """ Create experiment folder and store .ini inside"""
        self.active_exp = exp
        self.exp_date = str(datetime.datetime.now()).split('.')[0].replace(' ', '_')

        # create exp folder
        if 'name' not in exp:
            name = "exp_" + str(int(time.time()))
        else:
            name = exp['name']
        self.active_exp_abspath = os.path.join(self.abspath, name)
        tools.mkdir_p(self.active_exp_abspath)

        # store .ini
        with open(os.path.join(self.active_exp_abspath, self.exp_date + '_' + name) + '.ini', 'w+') as fd:
            fd.write(toml.dumps(exp))

        # Create a STATUS file if it doesn't exist already
        self.status_abspath = os.path.join(self.active_exp_abspath, 'STATUS')
        try:
            open(self.status_abspath, 'r').close()
            if os.stat(self.status_abspath).st_size == 0:
                raise IOError
        except IOError:
            with open(self.status_abspath, 'w') as fd:
                status = {
                        'done_freqs': [],
                        'done_transmissions': [],
                }
                fd.write(toml.dumps(status))

    def gen_signals(self):
        """ Generates the input signals for the active experiment"""
        generate_signals(
            exp=self.active_exp,
            exp_abspath=self.active_exp_abspath,
            status_abspath=self.status_abspath,
            exp_date=self.exp_date,
        )

    def begin_trans(self):
        """ """
        begin_transmission(
            exp=self.active_exp,
            exp_abspath=self.active_exp_abspath,
            status_abspath=self.status_abspath,
            exp_date=self.exp_date
        )


if __name__ == '__main__':
    cp = Campaign('/Users/fmagno/projs/sipLab/2019_oceantech/campaigns/2019.04.15/dsp_proj/config_v2.ini')
    cp.activate_experiment(cp.data['experiments'][0])
    cp.gen_signals()
    cp.begin_trans()
