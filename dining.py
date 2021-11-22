
import socket

HOST = 'localhost'  # Standard loopback interface address (localhost)
PORT = 1500       # Port to listen on 1500

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connection from ', addr , "(kitchen)")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)