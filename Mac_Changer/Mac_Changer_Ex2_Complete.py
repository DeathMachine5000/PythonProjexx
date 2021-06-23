#!/usr/bin/env python

# Import subprocesses for execution across multiple OSs

import subprocess

subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
