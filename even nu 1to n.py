num=int(input("enter the value of num:"))
evensumcount=0
for i in range(1,num+1):
    if(i%2==0):
        evensumcount=evensumcount+1
print(evensumcount,"is the count of even numbers")