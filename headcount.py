import numpy as np

seating = np.array([
[1,1,0,0,0,0,1,1],
[1,1,0,1,1,0,1,1],
[0,0,0,1,1,0,0,0],
[1,1,0,1,1,0,1,1],
[1,1,0,0,0,0,1,1]])

#note sure how input is given???
##############################################
# x = int(input())
# y = int(input())

# seating = np.full((x, y), 0)

# for i in range(x):
#     for j in range(y):
#         seating[i][j] = input()
##############################################

grid = [[i, j] for i in range(len(seating)) for j in range(len(seating[i]))]

def check_movement(position):
    if position[0] >= len(seating) or position[0] < 0 or position[1] >= len(seating[0]) or position[1] < 0:
        return False
    if seating[position[0]][position[1]] == 0:
        return False
    seating[position[0]][position[1]] = 0
    return True

def bfs(st = (0,0), groups=list(), seating=seating):
        q = [st]
        visited = {tuple(pos): False for pos in grid}
        visited[st] = True
        prev = {tuple(pos): None for pos in grid}

        group_count = 0
        sur = 0
        while q:
            node = q.pop(0)
            neighbors = tuple([pos for pos in [[node[0] + 1, node[1] + 1], [node[0] - 1, node[1] - 1], [node[0] + 1, node[1] - 1], [node[0] - 1, node[1] + 1],[node[0] + 1, node[1]], [node[0] - 1, node[1]], [node[0], node[1] + 1], [node[0], node[1] - 1]] if pos in grid])
            for next_node in neighbors:
                if check_movement(next_node) and not visited[tuple(next_node)]:
                    group_count = group_count + 1
                    q.append(tuple(next_node))
                    visited[tuple(next_node)] = True
                    prev[tuple(next_node)] = node

                    seating[node[0]][node[1]] = 0

        groups.append(group_count+1)
        return (groups, seating)

# print(seating)

groups = list()

while(True):
  st = ()
  cut = 0
  for i in range(len(seating)):
    for j in range(len(seating[i])):
      if(seating[i][j] == 1):
        st = (i,j)
        cut = 1
        break
    if(cut == 1):
      break
  if(cut == 0):
    break

  tup = bfs(st=st, groups=groups, seating=seating)

  groups = tup[0]
  seating = tup[1]

if(len(groups)==0):
  groups.append(0)

groups.sort(reverse=True)
print(f"{len(groups)} teams of {groups} totalling {sum(groups)}")
