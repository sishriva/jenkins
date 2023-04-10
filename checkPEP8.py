#!/usr/bin/env python3

import subprocess
import os

def check():
    result = subprocess.check_output("python3 -m pylint /home/netman/Documents/Lab9/netman_netconf_obj2.py | grep \'Your code has been rated\' | awk \'{print $7}\' | awk -F/ \'{print $1}\'",shell=True)
    result = float(result)
    if result < 5:
        os.system("exit 1")
    else:
        os.system("exit 0")


if __name__ == '__main__':
    check()
