#!/usr/bin/python3

import os
import sys
import socket


if sys.argv[1]:
        if os.path.exists("/mnt/c/" + sys.argv[1]):
                os.chdir("/mnt/c/" + sys.argv[1])
        else:
                print("Path does not exist")
                exit(1)
else:
        os.chdir("/mnt/c")
        exit(1)

HOST = ''
PORT = 50007
ADDR = HOST, PORT
BUFFER = 2048
BIGBUFFER = 8192
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
        c, *args = input("C:/" + os.getcwd()[7:] + "$ ").split(" ")
        if c == "q":
                break
        elif c == "cd":
                os.chdir(os.getcwd() + "/" + "".join(args))
        elif c == "w":
                c2, *args = args
                s.sendto(c2.encode() + b" " + b' '.join(a.encode() for a in args), ADDR)
                print("Receiving...")
                print(s.recvfrom(BIGBUFFER)[0].decode())
                while True:
                        check = int(s.recvfrom(BUFFER)[0].decode())
                        print(">>", check)
                        if not check:
                                break
                        print(s.recvfrom(BIGBUFFER)[0].decode())
        else:
                r = os.system(c + " " + " ".join(args))
                if r:
                        print(">>", r)
