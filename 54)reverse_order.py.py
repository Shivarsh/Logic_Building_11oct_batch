n=int(input("Enter A Number :"))
rev=0
rem=0
while n!=0:
    rem=int(n%10)
    rev=(rev*10)+rem
    n=int(n/10)

print(rev)