a=int(input('Primul numar: '))
b=int(input('Al doilea numar: '))
c=int(input('Al treilea numar: '))
if (a<b+c) and (b<a+c) and (c<a+b):
    if (a==b) or (b==c) or (a==c):
        print('Exista triunghi cu asa laturi si este isoscel')
    elif a==b==c:
        print('Exista triunghi cu asa laturi si este echilateral')
    else:
        print('Exista triunghi cu asa laturi si este scalen')
else:
    print('Nu exist[ triunghi cu laturile egale cu a,b si c')