import requests
from flask import Flask, request
import queue
import time
import threading
import logging
import random

class Waiter(threading.Thread):
    def __init__(self, waiter_id, name, *args, **kwargs):
        super(Waiter, self).__init__(*args, **kwargs)
        self.id = waiter_id
        self.name = name
        self.daemon = True

    def run(self):
        while True:
            self.search_order()

    def search_order(self):
        try:
            order = orders_queue.get()
            orders_queue.task_done()
            table_id = next((index for index, table in enumerate(tables_list) if table.id == order['table_id']), None)
            logging.info(
                f'{threading.current_thread().name} has taken the order with Id: {order["order_id"]} | priority: {order["priority"]} | items: {order["items"]} ')
            tables_list[table_id].state = STATUSES[2]
            payload = dict({
                'order_id': order['order_id'],
                'table_id': order['table_id'],
                'waiter_id': self.id,
                'items': order['items'],
                'priority': order['priority'],
                'max_wait': order['max_wait'],
                'time_start': time.time()
            })
            time.sleep(random.randint(2, 4) * TIME_UNIT)
            requests.post('http://localhost:8000/order', json=payload, timeout=0.0000000001)

def generate_order():
        (table_id, table) = next(
            ((id_number, table) for id_number, table in enumerate(tables_list) if table.state == STATUSES[0]),
            (None, None))
        if table_id is not None:
            max_wait_time = 0
            food_choices = []
            for i in range(random.randint(1, 5)):
                choice = random.choice(menu)
                if max_wait_time < choice['preparation-time']:
                    max_wait_time = choice['preparation-time']
                food_choices.append(choice['id'])
            max_wait_time = max_wait_time * 1.3
            neworder_id = generate_unique_id()
            neworder = {
                "order_id": neworder_id,
                "table_id": table.id,
                "items": food_choices,
                "priority": random.randint(1, 5),
                "max_wait": max_wait_time
            }
            orders_cache.append(neworder)
            orders_queue.put(neworder)
            tables_list[table_id].state = STATUSES[1]
            tables_list[table_id].order_id = neworder_id

        else:
            time.sleep(random.randint(2, 10) * TIME_UNIT)
            (table_id, table) = next(
                ((id_number, table) for id_number, table in enumerate(tables_list) if table.state == STATUSES[3]),
                (None, None))
            if table_id is not None:
                tables_list[table_id].state = STATUSES[0]

if __name__ == '__main__':
    threads = []
    main_thread = threading.Thread(target=lambda: app.run(host='0.0.0.0', port=3000, debug=False, use_reloader=False),
                                   daemon=True)