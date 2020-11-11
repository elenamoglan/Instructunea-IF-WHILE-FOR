#a
n=eval(input('Varsta lui Mihai este '))
s=1
cadou = 1
for i in range (1,n+1):
    cadou *= 2
    s += cadou + i
print(f'a) Mihai a primit {s} bani cand avea {n} ani')

#b
s = 1
i = 0
cadou = 1
while s<=100:
    i += 1
    cadou *= 2
    s += cadou + i
print(f'b) Cadoul a fost mai mare de 100$ cand Mihai avea {i} ani')
