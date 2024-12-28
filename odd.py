num=int(input("enter the value of num:"))
oddsumcount=0
for i in range(1,num+1):
    if(i%2!=0):
        oddsumcount=oddsumcount+1
print(oddsumcount,"is the count of odd numbers")