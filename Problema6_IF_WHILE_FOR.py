#a
n=eval(input('Introduceti numarul:'))
S1 = 0
S2 = 0
for i in range(1,n+1):
    S1 += i**3
    S2 += i
S2 **= 2
print(f'a) Prima suma este {S1}, iar a doua este {S2}')
if S1<S2:
    print('Prima suma este mai mica decat a doua')
elif S1>S2:
    print('Prima suma este mai mare decat a doua')
else:
    print('Sumele sunt egale')

#b
n=eval(input('Introduceti numarul:'))
S1 = 0
S2 = 0
for i in range(1,n+1):
    S1 += i**2
    S2 += i
S1 *= 3
S2 += n**3 + n**2 
print(f'b) Prima suma este {S1}, iar a doua este {S2}')
if S1<S2:
    print('Prima suma este mai mica decat a doua')
elif S1>S2:
    print('Prima suma este mai mare decat a doua')
else:
    print('Sumele sunt egale')