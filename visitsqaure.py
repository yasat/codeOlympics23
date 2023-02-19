import random
import matplotlib.pyplot as plt

board = [i for i in range(40)]

unique_squares = set()

num_rolls = 0
iter_rolls = 0
current_square = 0
iters = 0

iters_list = list()

while len(unique_squares) < 40:
    roll = random.randint(1, 6) + random.randint(1, 6)
    num_rolls = num_rolls + 1
    iter_rolls = iter_rolls + 1
    if(current_square + roll >= 40):
      iters = iters+1
      iters_list.append(iter_rolls)
      iter_rolls = 0
      current_square = 40 - (current_square + roll)
    else:
      current_square = (current_square) + roll
    unique_squares.add(board[current_square])
    
print(f"tt took {num_rolls} rolls and {iters} iterations.")


plt.figure(figsize=(22,6))
plt.plot(range(1,iters+1), iters_list)

plt.xlabel("iterations")
plt.ylabel("rolls")
plt.xticks(range(1,iters+1))
plt.title("rolls in each iteration")
