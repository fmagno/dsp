"""Useful tools"""
import errno
import math
import os


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


if __name__ == '__main__':
    fmin = geom2freq(D=200e-2, L=60e-2, ncycles=10.)
    print('freq min:', fmin)

