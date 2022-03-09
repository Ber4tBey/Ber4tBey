#Ber4tbey

import os
import time
try:
    import requests
except:
    os.system("pip install requests")
try:
    import sys
except:
    os.system("pip install sys")
try:
    os.system("clear")
    time.sleep(1)
    os.system("figlet Nano")
    link=input("Tool Linki Giriniz: ")
    req = requests.get(link).text
    os.system("clear")
    exec(req)
except:
    os.system("clear")
    os.system("figlet Nano")
    print("Bu Bir Nano Tool Linki Değildir!!!!")
    time.sleep(2)
    exit()
