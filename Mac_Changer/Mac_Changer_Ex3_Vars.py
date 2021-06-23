#!/usr/bin/env python

# Import subprocesses for execution across multiple OSs

import subprocess

interface = "eth0"
new_mac = "00:11:22:33:44:77"

print("[+] Changing MAC address for " + interface)
print("[+] Changing MAC address to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig  " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig " + interface, shell=True)