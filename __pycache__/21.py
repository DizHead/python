from random import shuffle

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4
shuffle(cards)

ypoints = 0
dpoints = 0
move = 1
more = 'да'
while more == 'да':
    if move == 1:
        dcard = cards.pop()
        dpoints += dcard

        ycards = []
    
        for i in range(2):
            ycard = cards.pop()
            ycards.append(ycard)
            ypoints += ycard
    else:    
        ycard = cards.pop()
        ycards.append(ycard)
        ypoints += ycard


    print(f'''
    -------------
    Очки:
    
    Крупъе: {dpoints}

    Вы: {ypoints}
    -------------
    ''')
   
    if move == 1:
        print(f'Вам выпали карты номиналом {ycards[0]} и {ycards[1]}')
    else:
        print(f'Вам выпала карта номиналом {ycard}')     

    if ypoints < 22:
        if ypoints == 21:
            more = 'нет'
        else:
            more = input('Ещё? Да или нет\n')
        move +=1
    else:
        print('Перебор')
        break
else:
    while dpoints < 18:
        dcard = cards.pop()
        dpoints += dcard
    print(f'''
    -------------
    Очки:
    
    Крупъе: {dpoints}

    Вы: {ypoints}
    -------------

    Крупъе выпала карта номиналом {ycard}    

    ''')

    if ypoints == dpoints:
        print('Ничья') 
    elif dpoints > 21:
        print('Крупъе проиграл. Перебор') 
    elif ypoints < dpoints:
        print('Вы проиграли. У крупъе число выше')  
    elif ypoints > dpoints:
        print('Вы выиграли. У Вас число выше')      
    elif dpoints == 21:
        print('Вы проиграли. У Крупъе блэкджек')
    elif ypoints == 21:
        print('Вы выиграли. У Вас блэкджек')
    elif ypoints > 21:
        print('Вы проиграли. Перебор')
          
        