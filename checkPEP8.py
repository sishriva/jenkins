#!/usr/bin/env python3

import subprocess
import os

result = subprocess.check_output("python3 -m pylint /home/netman/Documents/Lab9/netman_netconf_obj2.py | grep \'Your code has been rated\' | awk \'{print $7}\' | awk -F/ \'{print $1}\'",shell=True)
result = float(result)
if result < 10:
    print("PEP8 style code violation detected. Exiting....")
    exit(1)
else:
    print("Code complies with the PEP8 style. Continuing....")
    exit(0)

#if __name__ == '__main__':
#    check()
