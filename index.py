from hashlib import sha256
from itertools import permutations
from time import time 
import deco

tries = 0
start_time = time()

for res in permutations("ZjyOGzsKQ"):
  res = ''.join(res)
  string = "ctf{" + res + "}"
  Hash = sha256(string.encode()).hexdigest()
  #comment the line below to get a higher performance 
  print(Hash + "  :  " + res)
  tries +=1

  if(Hash == "327cad4cbe16f0a7aed9abf024b7fcdc37b684cee3369728f08e471176f94c25"):
    print(deco.center("="))
    print("hash: " + Hash)
    print("key: " + string)
    print("tries: " + str(round(tries / (time() - start_time))) + "p/s")
    print("\n")
    exit()
