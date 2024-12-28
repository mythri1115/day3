Num=int(input("enter the value"))
digitcount=0
#condition to get number of digit (num=25)
while(Num!=0):
    Num=Num//10
    digitcount=digitcount+1
print(digitcount,"digits")