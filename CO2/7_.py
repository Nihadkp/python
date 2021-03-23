#Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums to same value (c) whether any value occur in both
list1=[54,99,24,65,57,56]
list2=[54,65,57,41256,57,23,59]
if len(list1)==len(list2):
  print('same length')
else:
  print("not same")
total=sum(list1)
print('sum of the list1',total)
total=sum(list2)
print('sum of the list2',total)
print("numbers occuring in both")
for number in list1:
  if number in list2:
    print(number)