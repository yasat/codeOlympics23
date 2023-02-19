import numpy as np

maze = np.array([
['+', '-', '+', '-', '+', '-', '+'],
['|', ' ', ' ', ' ', ' ', ' ', '|'],
['+', ' ', '+', '-', '+', ' ', '+'],
['|', ' ', ' ', 'F', '|', ' ', '|'],
['+', '-', '+', '-', '+', ' ', '+'],
['|', '$', ' ', ' ', ' ', ' ', '|'],
['+', '-', '+', '-', '+', '-', '+']])

#note sure how input is given???
##############################################
# x = int(input())
# y = int(input())

# maze = np.full((x, y), "+")

# for i in range(x):
#     for j in range(y):
#         maze[i][j] = input()
##############################################

snake = (np.where(maze=="$")[0][0],np.where(maze=="$")[1][0])
food = (np.where(maze=="F")[0][0],np.where(maze=="F")[1][0])

grid = [[i, j] for i in range(len(maze)) for j in range(len(maze[i]))]

def check_movement(position):
    if position[0] >= len(maze) or position[0] < 0 or position[1] >= len(maze) or position[1] < 0:
        return False
    if maze[position[0]][position[1]] in ["+","-","|"]:
        return False
    return True

def bfs(snake, food):
        q = [snake]
        visited = {tuple(pos): False for pos in grid}
        visited[snake] = True
        prev = {tuple(pos): None for pos in grid}

        while q:
            node = q.pop(0)
            neighbors = tuple([pos for pos in [[node[0] + 1, node[1]], [node[0] - 1, node[1]], [node[0], node[1] + 1], [node[0], node[1] - 1]] if pos in grid])
            for next_node in neighbors:
                if check_movement(next_node) and not visited[tuple(next_node)]:
                    q.append(tuple(next_node))
                    visited[tuple(next_node)] = True
                    prev[tuple(next_node)] = node

        path = list()
        p_node = food

        start_node_found = False
        while not start_node_found:
            if prev[p_node] is None:
                return []
            p_node = prev[p_node]
            if p_node == snake:
                path.append(food)
                return path
            path.insert(0, p_node)

        return []

# print(maze)

path = bfs(snake, food)
dirs = list()
st = snake
for snake in path:          
  if(snake[0] == st[0]):
    if(snake[1] > st[1]):
      dirs.append("right")
    else:
      dirs.append("left")
  else:
    if(snake[0] > st[0]):
      dirs.append("down")
    else:
      dirs.append("up")
  st = snake

print(dirs)
