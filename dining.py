# Import socket module
import socket
import json
from table import orderGenerator, n_tables, max_dish
import random

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
    #message = "shaurya says geeksforgeeks"
    

    
    message_dining = "this message is sent from dining"
    message1 = message_dining + json.dumps(data1)
    i = 0
    while True:
        i += 1
        nitem = random.randint(1, max_dish)
        message1 = orderGenerator(i, nitem)
        print(nitem)
        message = json.dumps(message1)
        # message sent to server
        s.send(message.encode("ascii"))

        # messaga received from kitchen
        message_kitchen = s.recv(1024)

        # print the received message
        # print(str(message_kitchen.decode('ascii')))

        # ask the client whether he wants to continue
        # ans = input('\nDo you want to continue(y/n) :')
        # if ans == 'y':
        #     continue
        # else:
        #     break
    # close the connection
    s.close()

if __name__ == '__main__':
    Main()

