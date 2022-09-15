import socket
from telnetlib import SNDLOC
import time
import os
import hashlib

def get_rand_str_Hex(length):
    buf = ''
    while len(buf) < length:
        buf += hashlib.md5(os.urandom(100)).hexdigest()
    return buf[0:length]

HOST = "150.65.230.91"
PORT = 3361
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.settimeout(2)

count = 0
sendline1 = "150.65.230.114:029001:0xC0,"
sendline2 = "150.65.230.114:029002:0xC0,"
sendline3 = "150.65.230.114:029003:0xC0,"

print("Change Start!")

while True:
    s.settimeout(2)
    if (count > 5):
        break
    count += 1
    Color = get_rand_str_Hex(6)
    s.sendall((sendline1 + str(get_rand_str_Hex(6)) + "/n").encode())
    time.sleep(0.5)
    s.sendall((sendline2 + str(get_rand_str_Hex(6)) + "/n").encode())
    time.sleep(0.5)
    s.sendall((sendline3 + str(get_rand_str_Hex(6)) + "/n").encode())

    time.sleep(0.5)
print("Finish!")
