import random
import time

conditions = [
    lambda x: x % 2 == 0,
    lambda x: str(x).count('2') == 1,
    lambda x: x % 3 != 0,
    lambda x: str(x).count('8') == 0,
    lambda x: str(x).count('3') == 1,
    lambda x: x % 4 == 0,
    lambda x: x % 8 == 0,
    lambda x: str(x).count('4') == 1,
    lambda x: len(set(str(x))) == 4
]

a = 0
iter = 0

st = time.time()
while True:
  iter = iter + 1
  if(False not in [condition(a) for condition in conditions]):
    break
  a = random.randint(-10000000000, 10000000000)

print(a)
duration = time.time() - st
print(f"it took {iter} iterations and {duration} seconds to break out of loop")
