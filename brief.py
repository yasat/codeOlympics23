a = [[1,3,2,4,1], [3,1,2,4,3], [2,3,4,1,2], [2,1,4,3,1], [4,1,2,3,4]]

#note sure how input is given???
##############################################
# x = 5
# y = 5

# a = list()

# for i in range(x):
#     b = list()
#     for j in range(y):
#         b.append(int(input()))
#     a.append(b)
##############################################

rules = [[2,2,3,4], ["4", "prev_ind:1", 1, "prev_ind:1"], ["prev_lab:2", "prev_lab:1", 3, "4"], ["prev_ind:1", 1, "prev_ind:2", "prev_ind:2"], ["prev_ind:1", "prev_ind:2", "prev_ind:3", "prev_ind:4"]]

ind = []
rule=-1
key = ""

for i in a:
  rule = rule+1
  prompt = i[-1]
  r = rules[rule][prompt-1]
  if("lab" in str(r)):
    value = key[int(r.split(":")[1])-1]
    ind.append(a[int(r.split(":")[1])-1][0:-1].index(int(value)))
    key = key + value

  elif("ind" in str(r)):
    pos = ind[int(r.split(":")[1])-1]
    ind.append(pos)
    key = key + str(i[pos])

  elif(str(type(r))=="<class 'int'>"):
    ind.append(r-1)
    key = key + str(i[r-1])

  else:
    pos = i.index(r)
    ind.append(pos)
    key = key + r

print(key)
