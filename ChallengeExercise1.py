n = int(input("Please enter a number: "))
spacesCount = n-1
for i in range(1,n+1):
    for j in range(1,spacesCount+1):
        print(" ",end='')
    for k in range(1,2*i):
        if(k%2!=0):
            print("*",end='')
        else:
            print(" ",end='')
    spacesCount-=1
    print()