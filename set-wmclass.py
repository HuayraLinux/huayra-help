#!/usr/bin/env python
"""
Helper/hack para definir al hint WM_CLASS de una aplicacion.
"""

import shlex
import argparse
import subprocess as sp

VERSION = "0.1"


def version():
    "shows the current version"
    print VERSION


def usage():
    print "`{} -h` to view help".format(__file__)


def app_id(pid):
    "Obtains app id"
    return sp.check_output("wmctrl -lp|grep {}|cut -d ' ' -f1".format(pid), shell=True).strip()


def set_wmclass(pid, title):
    "Defines wm_class to a given `pid` and `title`"
    xprop = "xprop -id {} -f WM_CLASS 8s -set WM_CLASS '{}'".format(app_id(pid),title)
    return sp.call(shlex.split(xprop))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version',
                        action="store_true",
                        help=version.__doc__)
    parser.add_argument('-p', '--pid',
                        type=int,
                        help=set_wmclass.__doc__)
    parser.add_argument('-t', '--title',
                        type=str,
                        help=set_wmclass.__doc__)
    args = parser.parse_args()

    if args.pid and args.title:
        set_wmclass(args.pid, args.title)
    else:
        usage()
