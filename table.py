import random
import time

class table:
    def __init__(this, table_id, status, order_id):
        this.table_id = table_id
        this.state = status
        this.order_id = order_id

table_status = ["free", "making a order", "waiting for a order to be served"]
table_list = []
order_list = {}
n_tables = 10
max_dish = 4

def tableGenerator():
    i = 1
    while i <= n_tables:
        table_list.append(table(i, table_status[0], None))
        i += 1
        print(table_list)
    return table_list

def dish(d_number):
    dish_list = []
    i = 1
    while i <= d_number:
        dish_list.append(random.randint(1, 8))
        i += 1
        #print(dish_list)

    return dish_list

def calculate_max_wait(dishes):
    result = 0
    for x in dishes:
        max = 0
        max1 = 0
        if (x == 3): 
            max = 7
            if max > max1 :
                max1 = max
        if (x == 2): 
            max = 10
            if max > max1 :
                max1 = max
        if (x == 6): 
            max = 10
            if max > max1 :
                max1 = max
        if (x == 1): 
            max = 20
            if max > max1 :
                max1 = max
        if (x == 7): 
            max = 20
            if max > max1 :
                max1 = max
        if (x == 8): 
            max = 30
            if max > max1 :
                max1 = max
        if (x == 4): 
            max = 32
            if max > max1 :
                max1 = max
        if (x == 5): 
            max = 35
            if max > max1 :
                max1 = max
    result = max1 * 1.3
    return result


def orderGenerator(id, n):
    items = dish(n)
    order_list["id"] = id
    order_list["items"] = items
    order_list["priority"] = random.randint(1, 5)
    order_list["max_wait"] = calculate_max_wait(items)
    order_list["pick_time"] = time.time()

    time.sleep(1)
    return order_list

def appendOrderToTable(tables, order_id):
    nitem = random.randint(1, max_dish)
    order = orderGenerator(order_id, nitem)
    order_list["table_id"] = tables.table_id
    tables.state = table_status[1]
    tables.order_id = id
    time.sleep(1)
    return order

def tableMain(order_id):
    i = c = 1
    table_list.append(table(1, table_status[0], None))
    table_list.append(table(2, table_status[0], None))
    table_list.append(table(3, table_status[0], None))
    table_list.append(table(4, table_status[0], None))
    table_list.append(table(5, table_status[0], None))
    table_list.append(table(6, table_status[0], None))
    table_list.append(table(7, table_status[0], None))
    table_list.append(table(8, table_status[0], None))
    table_list.append(table(9, table_status[0], None))
    table_list.append(table(10, table_status[0], None))

    for tables in table_list:
        c +=1
        if tables.state == table_status[0]:
            order = appendOrderToTable(tables, order_id)
            return order
        if tables.state == table_status[1]:
            print("state 1")
        if  tables.state == table_status[2]:
            print("state 2")
