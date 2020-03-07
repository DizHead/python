def sum(*number):
    sum = 0
    for item in number:
        sum += item
    print('СУмма данных чисел равна ', sum)

sum()   

def privet(*name):
    for say in name:
        print('Привет', name)  

privet['Петя','Геральт','Артем']      
    