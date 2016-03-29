#!/usr/bin/env python
"""
Helper/hack para obtener el PID del proceso padre
del proceso padre que estamos ejecutando.
"""

import argparse
import subprocess as sp

VERSION = "0.1"


def version():
    "shows the current version"
    print VERSION


def usage():
    print "`{} -h` to view help".format(__file__)


def parent_pid(pid):
    "Obtains parent pid"
    return sp.check_output("ps -o ppid= -p {}".format(pid), shell=True)


def grandparent_pid(pid):
    "Obtains `grandparent's` pid"
    return parent_pid(parent_pid(pid)).strip()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version',
                        action="store_true",
                        help=version.__doc__)
    parser.add_argument('-p', '--pid',
                        type=int,
                        help=grandparent_pid.__doc__)
    args = parser.parse_args()

    if args.pid:
        print grandparent_pid(args.pid)
    else:
        usage()
