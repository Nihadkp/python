#construct the pattern using nested loop

for i in range(9):
    if(i<=4):
        j=0
        while j<=i:
            print(end='*')
            j+=1
        print(end='\n')
    else:
        j=8
        while j>=i:
            print(end='*')
            j-=1
        print(end='\n')


