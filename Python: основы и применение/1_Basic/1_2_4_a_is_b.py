
objects = [1,2,1,2,3,4,5,5,4,6,7,7,8,8]
ans = len(objects)

for obj in range(ans):
    for j in range(obj):
        if id(objects[obj]) == id(objects[j]):
            ans -=1
            break
print(ans)