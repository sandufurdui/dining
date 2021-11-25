# Dining
To get started, run the dining.py from https://github.com/sandufurdui/dining
(if you have installed locally python, run python dining.py)
then run kitchen from https://github.com/sandufurdui/dining (python kitchen.py)


Update
Improved data exchange between kitchen and dining, now each can send dictionaries(aka json)
Implemented threading.

#Output
PS D:\Users\sandu\Desktop\Python\PR\dining> python dining.py
Connection from  ('127.0.0.1', 60953) (kitchen)

PS D:\Users\sandu\Desktop\Python\PR\kitchen> python .\kitchen.py        
Received: b'dining hall up at localhost:1500'



