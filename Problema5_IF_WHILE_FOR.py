an=eval(input('Anul este '))
an -= 2000
rest = an % 12
if rest == 0:
    print('Anul poarta numele de dragon')
elif rest == 1:
    print('Anul poarta numele de sarpe')
elif rest == 2:
    print('Anul poarta numele de cal')
elif rest == 3:
    print('Anul poarta numele de oaie')
elif rest == 4:
    print('Anul poarta numele de maimuta')
elif rest == 5:
    print('Anul poarta numele de cocos')
elif rest == 6:
    print('Anul poarta numele de caine')
elif rest == 7:
    print('Anul poarta numele de porc')
elif rest == 8:
    print('Anul poarta numele de sobolan')
elif rest == 9:
    print('Anul poarta numele de bou')
elif rest == 10:
    print('Anul poarta numele de tigru')
else:
    print('Anul poarta numele de iepure')