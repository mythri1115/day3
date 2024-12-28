num=int(input("enter the value:"))
sumdigits=0
rem=0
while(num!=0):
    rem=num%10
    sumdigits=sumdigits+rem
    num=num//10
print("sum of digits are:",sumdigits)
        