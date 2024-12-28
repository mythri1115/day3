num=int(input("enter the integer value:"))
evensum=0
oddsum=0
for i in range(1,num+1):
    if(i%2==0):
        evensum=evensum+1
    else:
        oddsum=oddsum+1
print("even sum",evensum)
print("odd sum",oddsum)
    