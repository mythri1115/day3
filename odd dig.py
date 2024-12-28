num=int(input("enter the value:"))
odddigitcount=0
rem=0
#condition to get number of odd digit (num=12345)
while(num!=0):
    rem=num%10
    if(rem%2!=0):
        odddigitcount+=1 #odddigitcount+1
        num=num//10
print("no of odd digits are",odddigitcount)