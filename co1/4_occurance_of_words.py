#Count the occurrences of each word in a line of text.
text=input("Enter the line : ")
for i in text.strip().split():
    print("Number of occurence of word ","\"",i,"\""," is :",text.strip().split().count(i))

