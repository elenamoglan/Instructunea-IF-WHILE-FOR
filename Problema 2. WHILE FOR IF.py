
n=int(input("n="))
s=0
p=1
for i in range(1, n+1):
    p*=n
    n-=1
    s+=p
print("Suma ", s)