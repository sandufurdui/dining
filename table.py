import random


class table:
    def __init__(this, id, name):
        this.tableId = id
        this.tableName = "table_" + str(name)

class order:
    def __init__(this, id, items, priority, max_wait):
        this.orderId = id
        this.items = items
        this.priority = priority
        this.max_wait = max_wait

table_list = []
order_list = {}
n_tables = 4
max_dish = 10
order_id = 1
wait = 1
dish_number = random.randint(1, max_dish)

def tableGenerator():
    i = 1
    while i <= n_tables:
        table_list.append(table(i, i))
        i += 1
        # x = random.randint(1, max_dish)

    # for test in table_list :
    # print( test.tableId, test.tableName, sep =' ' )

    return table_list

def dish():
    dish_list = []
    i = 1
    while i <= dish_number:
        dish_list.append(random.randint(1, max_dish))
        i += 1
        #print(dish_list)

    return dish_list

items = dish()
# def orderGenerator():
#     i = 1
#     order_list.append(order(order_id , 0 , random(1, 5), wait))
#     order_list["items"] = dish
#     return order_list

def orderGenerator(id):
    i = 1
    order_list["id"] = id
    order_list["items"] = items
    order_list["priority"] = random.randint(1, 5)
    order_list["max_wait"] = random.randint(1, 300)

    print(order_list)
    return order_list

