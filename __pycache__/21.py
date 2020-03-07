from random import shuffle

cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4
shuffle(cards)

ypoints = 0
dpoints = 0
move = 1
more = 'да'
while more == 'да':
    dcard = cards.pop()
    dpoints += dcard

    ycards = []
    if move == 1:
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
        print(f'Вам выпала карта номиналом {ycards[0]}')     

    if ypoints & dpoints < 22:
        if ypoints == 21 or dpoints == 21:
            if ypoints == 21:
                print('Блэкджек! Вы выиграли')
            else:
                print('Блэкджек у противника! Вы проиграли')
        elif ypoints == dpoints:
            print('Ничья')  
            break
        elif ypoints < dpoints:
            print('Вы проиграли')
            break
        elif ypoints > dpoints:
            more = input('Еще? да или нет\n')
            if not more:
                if ypoints > dpoints:
                    print('Вы выиграли')
                    break
    else:
        if ypoints < 21:
            print('Вы выиграли')            
   
        
    move += 1