# create a single string seperated with space from two strings by swapping the charecter at position 1

str1 = "apple"
str2 = "orange"
str1_list = list(str1)
str2_list = list(str2)
temp = str1_list[1]
str1_list[1] = str2_list[1]
str2_list[1] = temp
print("Before exchanging elements:", str1, str2)
print("string after exchanging charecter at position 1:", "".join(str1_list), "".join(str2_list))
