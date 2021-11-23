import socket
import pickle

HEADERSIZE = 30
host = 'localhost'
port = 4000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(450)
        if new_msg:
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(pickle.loads(full_msg[HEADERSIZE:])) #decodes the message
            new_msg = True
            full_msg = b""