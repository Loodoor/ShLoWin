#!/usr/bin/python3

import os
import sys
import socket


# intercepting command line arguments
if sys.argv[1:]:
        if sys.argv[1] != '-h':
                if os.path.exists("/mnt/c/" + sys.argv[1]):
                        os.chdir("/mnt/c/" + sys.argv[1])
                else:
                        print("Path does not exist. Setting path to /mnt/c")
                        os.chdir("/mnt/c/")
        else:
                print("""Help message for ShLoWin
Version 0.0.1
usage : cwin.py [path]
 - path should be a valid path to a Windows folder, refering to C:\\
        ex: cwin.py Users => start a shell in C:\\Users

""")
else:
        os.chdir("/mnt/c")

# some constants
HOST = ''  # on localhost
PORT = 50007
ADDR = HOST, PORT
BUFFER = 2048
BIGBUFFER = 8192
PS1 = "$"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
        c, *args = input(os.getcwd()[5:6] + ":/" + os.getcwd()[7:] + PS1 + " ").split(" ")
        if c == "q":
                break
        elif c == "ps1":
                PS1 = *args[0:1] if args[0:1] else PS1
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
