#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead.
list = []
l = int(input("Enter the limit:"))
for x in range(l):
    num = int(input("Enter number " + str(x + 1) + ":"));
    if (num > 100):
        num = "over"
    list.append(num)
print(list)