import socket
import time

HOST = "150.65.230.91"
PORT = 3361
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.settimeout(2)

d = 0
count = 0
while True:
    s.settimeout(2)
    if (count > 10):
        break
    if (d == 0):
        print("Light ON\n")
        sendline = b"150.65.230.114:029000:0x80,0x30\n"
        d = 1
    elif (d == 1):
        print("Light OFF\n")
        sendline = b"150.65.230.114:029000:0x80,0x31\n"
        d = 0
        count += 1
    s.send(sendline)
    time.sleep(0.5)
