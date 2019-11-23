# Программа для автоматизации навыков счёта
from time import sleep
from random import randint, choice
from timeit import default_timer


def time_endings(digit):
    digit = str(digit)
    last_digit = digit[-1]

    if digit == 11:
        return ''
    else:
        if last_digit == 1:
            return 'у'
        elif 1 < int(last_digit) < 5:
            return 'ы'
        else:
            return ''

def select_mode():
    mode = ''

    print('''Выбери режим
        1 = Тренировка
        0 = Выход''')

    mode = input()

    while mode not in {'0', '1'}:
        print("Нужно написать 0 или 1")
        mode = input()

    return mode




def count():

    print('Привет! Меня зовут Роджер. А как тебя?')
    name = input()
    name = name.title()

    print('Приятно познакомиться, ' + name)
    sleep(1)
    print('Давай проверим твои знания в математике.')
    sleep(1)

    answers_quantity = ''  # количество примеров
    maximum_answer = ''  # до скольки будет считать
    question = ''
    correct_answers = 0
    fails = 0
    time_in_seconds = 0
    seconds = 0
    minutes = 0


    while not answers_quantity.isdigit():
        print(name + ", сколько примеров ты готов решить?")
        answers_quantity = input()

        if answers_quantity.isdigit():
            while int(answers_quantity) < 1:
                print("Введи число больше 0")
                answers_quantity = input()
                while not answers_quantity.isdigit():
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
            print("Пример " + str(question + 1))

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
            print("сколько будет " + str(numeric1) + str(sign) + str(numeric2))

            start = default_timer()
            student_answer = input()
            stop = default_timer()

            time_in_seconds += round(stop - start)

            while not student_answer.isdigit():
                print("Должна быть цифра")
                student_answer = input()

            if int(student_answer) == correct_answer:
                print("Правильно,молодец!")
                correct_answers += 1
            else:
                print("Неправильно")
                print("Правильный ответ: " + str(correct_answer))
                fails += 1
                with open(f'{name}errors.txt','а') as f:
                    f.write('{number 1}{sign}{number 2} 3')

    if time_in_seconds < 60:
        spend_time = f"{time_in_seconds} секунд{time_endings(time_in_seconds)}"
    else:
        minutes = time_in_seconds // 60
        seconds = time_in_seconds - (minutes * 60)

        if seconds > 0:
            spend_time = f"{minutes} минут и {seconds} секунд"

    if fails == 0:
        print(f"Молодец, {name}, ты правильно ответил на все вопросы за {spend_time}.")
    elif correct_answers == 0:
        print(f"Ты не ответил ни на один вопрос правильно, затратив на это {spend_time}")
    else:
        print("Правильных ответов:" + str(correct_answers))
        print(f"Ошибок {fails}")
        print(f"Ты ответил за {spend_time}")

while True:

    mode = select_mode()

    if mode == '1':
        count()
    elif mode == '0':
        break
    else:
        pass

