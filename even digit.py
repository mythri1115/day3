num=int(input("enter the value:"))
evendigitcount=0
rem=0
#condition to get number of even digit (num=12345)
while(num!=0):
    rem=num%10
    if(rem%2==0):
        evendigitcount+=1 #evendigitcount+1
        num=num//10
print("no of even digits are",evendigitcount)