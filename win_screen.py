import time
import os
time.sleep(0.1)

inf = 0
jle = ":("



while inf == 0:

  
  with open("data/display.data") as file:
    int_number = file.read()
    print(int_number)
  with open("data/cls.data") as fie:
    in_number = fie.read()
    if in_number == "1":
      os.system("cls")
  
  
  
  time.sleep(0.05)
  
