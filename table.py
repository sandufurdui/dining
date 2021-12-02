import threading
import random
import time

class Table(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)

    def run(self):
        while True:
            time.sleep(1)
            self.generate_order()

    @staticmethod
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