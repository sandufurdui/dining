import socket, json
from waiter import getOrder
from table import tableMain
from _thread import *



def Main():
    id = 0
    while True:
        # local host IP '127.0.0.1'
        host = 'localhost'
        # Define the port on which you want to connect
        port = 8000
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # connect to kitchen on local computer
        s.connect((host,port))

        #while True:
        id += 1
        #main()
        mess_from_dining = tableMain(id)
        mess_from_dining_dumped = json.dumps(mess_from_dining)
            # message sent to kitchen
        s.send(mess_from_dining_dumped.encode("ascii"))

            # messaga received from kitchen
        message_kitchen_encoded = s.recv(1024)
        message_kitchen_decoded = str(json.loads(message_kitchen_encoded.decode('ascii')))


            
        # close the connection
    #s.close()

if __name__ == '__main__':
    Main()

