count = 0
items = [0,1,0,1,0]

for i in range(0, len(items)):
    if items[i] == 0:
        count += 1

print(count, len(items))
