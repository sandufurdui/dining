import random
import time

class table:
    def __init__(this, id, name):
        this.tableId = id
        this.tableName = "table_" + str(name)

# class order:
#     def __init__(this, id, items, priority, max_wait):
#         this.orderId = id
#         this.items = items
#         this.priority = priority
#         this.max_wait = max_wait

table_list = []
order_list = {}
n_tables = 4
max_dish = 4

def tableGenerator():
    i = 1
    while i <= n_tables:
        table_list.append(table(i, i))
        i += 1
        # x = random.randint(1, max_dish)

    # for test in table_list :
    # print( test.tableId, test.tableName, sep =' ' )

    return table_list

def dish(d_number):
    dish_list = []
    i = 1
    while i <= d_number:
        dish_list.append(random.randint(1, 8))
        i += 1
        #print(dish_list)

    return dish_list
    # for x in dishes:
    #     match dishes:
    #         case 1:
    #             result += 20
    #         case 2:
    #             result += 10
    #         case 3:
    #             result += 7
    #         case 4:
    #             result += 32
    #         case 5:
    #             result += 35
    #         case 6:
    #             result += 10
    #         case 7:
    #             result += 20
    #         case 8:
    #             result += 30

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
    i = 1
    items = dish(n)
    order_list["id"] = id
    order_list["items"] = items
    order_list["priority"] = random.randint(1, 5)
    order_list["max_wait"] = calculate_max_wait(items)
    
    #print(items) # print the order
    time.sleep(1)
    return order_list

