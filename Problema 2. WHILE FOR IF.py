import math
n=int(input("n="))
s=0
for i in range(1, n+1):
    s+=math.factorial(i) 
print("Suma este ", s)
