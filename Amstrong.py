n=int(input("Enter a number:"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if n==sum:
   print(n,"is an Amstrong number")
else:
    print(n,"is not an Amstrong number")


