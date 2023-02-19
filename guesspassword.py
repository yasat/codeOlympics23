def commons(relations, uniques):
    found = dict()
    for unique in uniques:
        for key in relations.keys():
            if(len(relations[key]) == 0):
                relations.pop(key)
                for key1 in relations.keys():
                    relations[key1].remove(key)
                return (key, relations)
            if(unique in relations[key]):
                found[key] = found.get(key,0) + 1
    
    found_value = [key for key, value in found.items if len(relations) == value][0]
    
    for key in relations.keys():
        relations[key].remove(found_value)
    
    return (found_value, relations)

def relationsfinder(token, keys):
    start = set()
    for key in keys:
        if token in key:
            for digit in key:
                if digit == token:
                    break
                else:
                    start.add(digit)
    return start


file = open('keylog.txt')
keys = list()

passcode = ""

keys = [key.strip() for key in file]
keys = set(keys)

uniques = set([digit for key in keys for digit in key])

relations = dict()

for key in uniques:
    relations[key] = relationsfinder(str(key), keys)

while len(relations)!=0:
    tup = commons(relations, uniques)
    found = tup[0]
    relations = tup[1]
    passcode = passcode + found
print(passcode)
