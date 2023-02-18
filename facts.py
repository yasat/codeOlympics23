import random

interesting_facts = {"Statue of Unity":790, "Laykyun Sekkya":424, "Great Buddha of Thailand":300, "Guanyin of Mount Xiqiao":203, "Burj Khalifa":2717, "world trade center":1776, "taipei":1667, "Tupolev ANT-20":108}

size = input()
or_size= size

fact = random.randint(0, len(interesting_facts)-1)

if("ft" in size):
  size = int(size.split("ft")[0])
  d = size // list(interesting_facts.values())[fact]
  c = int(list(interesting_facts.values())[fact]//size)+1
  
elif("cm" in size):
  size = int(size.split("cm")[0])
  d = (size*0.0328084) // list(interesting_facts.values())[fact]
  c = int(list(interesting_facts.values())[fact]//(size*0.0328084))+1

elif("mt" in size):
  size = int(size.split("mt")[0])
  d = (size*3.28084) // (list(interesting_facts.values())[fact])
  c = int(list(interesting_facts.values())[fact]//(size*3.28084))+1
# print(c)
if(d!=0):
  print(str(or_size), "is nearly {0} times of {1}".format(d, list(interesting_facts.keys())[fact]))
elif(c==1):
  print(str(or_size), "is nearly 1 time of {0}".format(list(interesting_facts.keys())[fact]))
else:
  print(str(or_size), "is nearly 1/{0} times of {1}".format(c, list(interesting_facts.keys())[fact]))
