<<<<<<< Updated upstream

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
=======
# Import socket module
import socket
import json
import sys


def Main():
    # local host IP '127.0.0.1'
    host = 'localhost'

    # Define the port on which you want to connect
    port = 8000

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # connect to server on local computer
    s.connect((host,port))
    with open("order.json", "r") as menu_json:
        data1 = json.load(menu_json)
    # message you send to server
    message = "shaurya says geeksforgeeks"
    
    
    data1 = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    message1 = json.dumps(data1)
    message_dining = "this message is sent from dining"
    while True:

        # message sent to server
        s.send(message1.encode("ascii"))

        # messaga received from kitchen
        message_kitchen = s.recv(1024)

        # print the received message
        print(str(message_kitchen.decode('ascii')))

        # ask the client whether he wants to continue
        ans = input('\nDo you want to continue(y/n) :')
        if ans == 'y':
            continue
        else:
            break
    # close the connection
    s.close()

if __name__ == '__main__':
    Main()

>>>>>>> Stashed changes
