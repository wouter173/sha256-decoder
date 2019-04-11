from hashlib import sha256
from itertools import permutations
import deco

for res in permutations("ZjyOGzsKQ"):
  res = ''.join(res)
  string = "ctf{" + res + "}"
  Hash = sha256(string.encode()).hexdigest()
  print(Hash + "  :  " + res)

  if(Hash == "327cad4cbe16f0a7aed9abf024b7fcdc37b684cee3369728f08e471176f94c25"):
    print(deco.center("="))
    print("hash: " + Hash)
    print("key: " + string)
    print("\n")
    exit()
