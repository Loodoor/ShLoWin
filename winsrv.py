import io
import os
import sys
import socket


old_stdout = sys.stdout
sys.stdout = mystdout = io.StringIO()

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
BUFFER = 2048
BIGBUFFER = 8192

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print("Started on localhost", PORT, file=old_stdout)

while True:
    # receiving
    data, addr = conn.recvfrom(BUFFER)
    print("Received {", data.decode(), "} from L-o-W", file=old_stdout)
    # executing request on windows
    ret = os.popen(data.decode()).read()
    ret = mystdout.getvalue() + "\n" + str(ret)
    # sending process
    try:
        conn.sendto(ret.encode()[:BIGBUFFER], addr)
        while len(ret.encode()) > BIGBUFFER:  # if len(ret) <= 8192, we skip and send 0  ___
            conn.sendto(str(1).encode(), addr)   # return code "it is not finished"        |
            ret = ret[BIGBUFFER:]                # truncate                                |
            conn.sendto(ret.encode[:BIGBUFFER], addr)  # send                              |
        conn.sendto(str(0).encode(), addr)       # return code "okay"  /___________________|
    except ConnectionAbortedError:
        print("Connection was reset")
        exit(1)
    
    mystdout.truncate(0)

sys.stdout = old_stdout