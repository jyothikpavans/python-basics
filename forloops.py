a= int(input("Please Enter a number: "))

c= int(input("No of times number should be reduced by 1 : "))

for i in range(a,a-c,-1):
    print(i," ",end='')
