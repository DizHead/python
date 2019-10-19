# Программа для автоматизации навыков счёта
from timeit import default_timer
from time import sleep
from random import randint, choice


print('Привет! Меня зовут Роджер. А как тебя?')
name = input()
name = name.title()

print('Приятно познакомиться, ' + name)
sleep(1)
print('Давай проверим твои знания в математике.')
sleep(1)
print('Ты готов? (да или нет)')

ready = input()

while ready not in {'да', 'нет'}:
    print('''Должно быть 'да' или 'нет'
Введи заново''')
    ready = input()

if ready == 'да':

   answers_quantity = ''  # количество примеров
   maximum_answer = ''  # до скольки будет считать
   question = ''


   while not answers_quantity.isdigit():
       print(name + ", сколько примеров ты готов решить?")
       answers_quantity = input()

       if answers_quantity.isdigit():
           while int(answers_quantity) < 1:
               print ("Введи число больше 0")
               answers_quantity = input()
               while not maximum_answer.isdigit():
                   print("Должна быть цифра")
                   answers_quantity = input()
       else:
           print("Должна быть цифра")

   while not maximum_answer.isdigit():
       print("До скольки будем считать")
       maximum_answer = input()

       if maximum_answer.isdigit():
           while int(maximum_answer) < 2:
               print("Введи число больше 1")
               maximum_answer = input()
               while not maximum_answer.isdigit():
                   print("Должна быть цифра")
                   maximum_answer = input()
       else:
           print("Должна быть цифра")

       for question in range(int(answers_quantity)):
           print("Пример " + str(question+1))

           # случайным образом сгенерируем
           numeric1 = randint(1, int(maximum_answer))  # левый операнд
           numeric2 = randint(1, int(maximum_answer))  # правый операнд
           sign = choice('+-')  # арифметический оператор

           # вычислим результат в зависимости от операции
           if sign == '-':
               # исключим отрицательный ответ
               while numeric1 < numeric2:
                   numeric1 = randint(1, int(maximum_answer))

               correct_answer = numeric1 - numeric2
           if sign == '+':
               # исключим превышение максимально допустимого ответа
               while numeric1 + numeric2 > int(maximum_answer):
                   numeric1 = randint(1, int(maximum_answer))  # левый операнд
                   numeric2 = randint(1, int(maximum_answer))  # правый операнд
               correct_answer = numeric1 + numeric2
           print("сколько будет " + str(numeric1) +str(sign) +str(numeric2))
           student_answer = input()
           if int(student_answer) == correct_answer:
               print("Правильно,молодец!")
           else:
               print("Неправильно")
               print("Правильный ответ: " + str(correct_answer))

if ready == 'нет':
    print('''Передумал? Хорошо, может как-нибудь в следующий раз...
Пока!''')