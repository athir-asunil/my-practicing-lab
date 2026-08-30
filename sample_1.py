Number=int(input("Enter a number  "))
Sum=0
count=0
for i in range(1,Number+1):
    if(i%2==0):
        Sum+=i
        count+=1
print("Sum of even numbers  ",Sum)
print("Number of even numbers ",count)
