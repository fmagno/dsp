"""Useful tools"""
import errno
import math
import os
import numpy as np
from scipy import signal


def geom2freq(D, L, ncycles, vel_water=1498.):
    """Calculates the minimum frequency required to avoid superposition
    between the direct path wave and the shortest reflected wave

                          -\                       ^
                        -/| -\                     |
                      -/  |   -\                   |
                    -/    |     -\                 |
            X     -/      |       -\               |
                -/        |         -\    X        | D
              -/          |           -\           |
            -/            |             -\         |
          -/              |               -\       |
        -/            +---|                 -\     |
      -/              |   |                   -\   |
    -/                |   |                     -  v
    T  ----------------------------------------  R
    <------------------------------------------->
                        L
    """
    fmin = int(
        ncycles * vel_water / (
            2 * math.sqrt(
                (L/2.)**2 + D**2
            ) - L
        )
    )
    return fmin


def mkdir_p(dirname):
    """ Equivalent to `mkdir -p <dirname>` """
    try:
        os.mkdir(dirname)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass


def fft(data, fs):
    """ Computes FFT """
    N = len(data)
    Y = np.fft.fft(data) / N
    Yabs = np.abs(Y)
    Yang = np.angle(Y)
    F = np.fft.fftfreq(N, 1./fs)
    Froll = np.fft.fftshift(F)
    Yabs_roll = np.fft.fftshift(Yabs)
    return Froll, Yabs_roll


def high_pass(data, cutoff=200., fs=250000., order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    y = signal.filtfilt(b, a, data)
    return y


if __name__ == '__main__':
    fmin = geom2freq(D=200e-2, L=60e-2, ncycles=10.)
    print('freq min:', fmin)

