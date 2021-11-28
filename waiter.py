import threading, logging
from table import tableMain

class Waiter(threading.Thread):
    def __init__(self, waiter_id, name, *args, **kwargs):
        super(Waiter, self).__init__(*args, **kwargs)
        self.id = waiter_id
        self.name = name
        self.daemon = True
    
def getOrder():
    threads = []
    
    while True:
        id = 0 
        payload = tableMain(id)
        id += 1
        return payload

def main():
    getOrder()
        
    # q = Queue.Queue()
    # t1 = threading.Thread(target=fill_q,args(q, lst))
    # t2 = threading.Thread(target=consume_q,args(q, lst))
    # t1.start()
    # t2.start()

    # def fill_q(q, lst):
    #     for elem in lst:
    #         q.put(elem)

    # def consume_q(q, lst):
    #     for i in range(len(lst)):
    #         send_to_server(q.get())