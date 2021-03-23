#Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.
old_str= input("Enter a string: ")
i = 0
new_list=list(old_str)
while i < len(new_list):
    j = 0;
    while j < i:
        if new_list[i].isspace():
           break
        elif new_list[i] == new_list[j]:
            new_list[i]="$"
            break
        else:
            j += 1
    i += 1;

print("formatted string is:","".join(new_list))
