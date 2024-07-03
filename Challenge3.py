# write a program to display sum of odd numbers and even numbers between 12 and 37 including both.
#Answer--
#sum_even=0
#sum_odd=0

#for i in range(12,38):
   # if i%2==0:
        #sum_even=sum_even+i
    #else:
       # sum_odd=sum_odd+i
#print(" sum of odd numbers is: ",sum_odd," sum of even numbers: ",sum_even)

#Write a program to display all the numbers that are divisible by 11 but not by 2 between 100 and 500
#Answer--
#for i in range(100,500):
 #   if i%11==0 and i%2!=0:
   #     print("The sequence of numbers that are divisible by 11 but not by 2 is: ",i)
   # else:
    #    contin
n = int(input("Please Enter a number: "))
count=0
for i in range(1,n+1):
    for j in range(1,i+1):
        count += 1
        print(count," ",end='')
    print()

















