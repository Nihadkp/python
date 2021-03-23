#Create a string from given string where first and last characters exchanged. [eg: python -> nythop]
str=input("Enter a string:")
str_list=list(str)
temp=str_list[0]
str_list[0]=str_list[-1]
str_list[-1]=temp
print("The the string after exchange first and last charecter:","".join(str_list))
