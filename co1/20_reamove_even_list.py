list1 = [113,54,95,57,32,25,2,5,98]
print(list1)
for i in list1:
    if i % 2 == 0:
        list1.remove(i)

print(list1)
