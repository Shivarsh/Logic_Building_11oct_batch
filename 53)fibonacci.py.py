num=int(input("Enter A Number:"))
n=0
n1=1
print(n)
print(n1)


for i in range(2,num):
    n2=n+n1
    n,n1=n2,n
    print(n2)

