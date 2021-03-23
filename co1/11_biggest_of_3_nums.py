#Find biggest of 3 numbers entered.
a = int(input("Enter 3 numbers:"))
b = int(input())
c = int(input())
if (a > b) and (a > c):
    print(a, "is largest number")
elif (b > a) and (b > c):
    print(b, "is largest number")
else:
    print(c, "is largest number")
