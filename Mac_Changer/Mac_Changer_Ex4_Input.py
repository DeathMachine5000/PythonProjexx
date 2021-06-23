#!/usr/bin/env python

# Import subprocesses for execution across multiple OSs

import subprocess

interface = input("Interface > ")
new_mac = input("New MAC > ")

print("[+] Changing MAC address for " + interface)
print("[+] Changing MAC address to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig  " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig " + interface, shell=True)