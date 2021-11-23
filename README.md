# Dining
To get started, run the dining.py from https://github.com/sandufurdui/dining
(if you have installed locally python, run python dining.py)
then run kitchen from https://github.com/sandufurdui/dining (python kitchen.py)

last commit in 40% branch has all set for 40% check </br>
-basic connection between 2 web servers(kitchen and dining)
-sending json(menu.json) file between servers

#Output
PS D:\Users\sandu\Desktop\Python\PR\dining> py .\dining.py
full message length: 404
434
full message received
[{'id': 1, 'name': 'pizza', 'preparation-time': 20, 'complexity': 2, 'cooking-apparatus': 'oven'}, {'id': 2, 'name': 'salad', 'preparation-time': 10, 'complexity': 1, 'cooking-apparatus': None}, {'id': 3, 'name': 'zeama', 'preparation-time': 7, 'complexity': 1, 'cooking-apparatus': 'stove'}, {'id': 4, 'name': 'Scallop Sashimi with Meyer Lemon Confit', 'preparation-time': 32, 'complexity': 3, 'cooking-apparatus': None}, {'id': 5, 'name': 'Island Duck with Mulberry Mustard', 'preparation-time': 35, 'complexity': 3, 'cooking-apparatus': 'oven'}, {'id': 6, 'name': 'Waffles', 'preparation-time': 10, 'complexity': 1, 'cooking-apparatus': 'stove'}, {'id': 7, 'name': 'Aubergine', 'preparation-time': 20, 'complexity': 2, 'cooking-apparatus': None}, {'id': 8, 'name': 'Lasagna', 'preparation-time': 30, 'complexity': 2, 'cooking-apparatus': 'oven'}]

PS D:\Users\sandu\Desktop\Python\PR\kitchen> py .\kitchen.py
Connection from ('127.0.0.1', 56353) has been established.



