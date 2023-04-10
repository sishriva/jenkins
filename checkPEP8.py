#!/usr/bin/env python3

import subprocess
import os

# result will store the score of pylint PEP8 code style
result = subprocess.check_output("python3 -m pylint /home/netman/Documents/Lab9/netman_netconf_obj2.py | grep \'Your code has been rated\' | awk \'{print $7}\' | awk -F/ \'{print $1}\'",shell=True)

#result will store the value in float
result = float(result)

#Jenkins should proceed further only if quality control is 5
if result < 5:
    print("PEP8 style code violation detected. Fix the violations to continue. Exiting....")
    exit(1)
else:
    print("Code complies with the PEP8 style. Continuing....")
    exit(0)
