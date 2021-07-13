#!/usr/bin/env python

# Import subprocesses for execution across multiple OSs
# Python 3 function used (input) --must run w/ python3
# Addresses insecurity in subprocess strings to prevent from executing additional Linux commands during user input
# Adds option parsing to create help menu and options for user input. 

import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Sets network interface to be changed.")
parser.add_option("-m", "--mac", dest="new_mac", help="Sets new MAC address.")
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface)
print("[+] Changing Mac address to " + new_mac)


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig", interface])
