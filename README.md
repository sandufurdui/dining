# Dining
To get started, run the dining.py from https://github.com/sandufurdui/dining
(if you have installed locally python, run python dining.py)
then run kitchen from https://github.com/sandufurdui/kitchen (python kitchen.py)


Update
Improved data exchange between kitchen and dining, now each can send dictionaries(aka json)
Implemented threading.

Update.v.1.2
-added order generator <br />
-now each table, regardless of its status is generating order and sending directly to kitchen

#Output
PS D:\Users\sandu\Desktop\Python\PR\dining> py .\dining.py              
this is the message sent from kitchen
{"brand": "chevrolet", "model": "camaro", "year": 2001}

Do you want to continue(y/n) :n

PS D:\Users\sandu\Desktop\Python\PR\kitchen> py .\kitchen.py
socket binded to port 8000
kitchen is listening
this message is sent from dining
{"brand": "Ford", "model": "Mustang", "year": 1964}

closing connection



