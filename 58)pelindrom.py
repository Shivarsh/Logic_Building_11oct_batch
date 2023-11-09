n=int(input("Enter A Number :"))
rev=0
rem=0
num=n
while n!=0:
    rem=int(n%10)
    rev=(rev*10)+rem
    n=int(n/10)

print(rev)
if rev==num:
    print("Number Is Pelindrome")

else:
    print("Given Number Is Not Pelindrome")


