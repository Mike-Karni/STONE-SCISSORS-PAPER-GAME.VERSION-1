# Камень ножницы бумага первая версия

import random
compScore = 0
userScore = 0
while True:

    userChoise = input("Введите число от 0 для камня,1 для бумаги,2 для ножниц ")
    if userChoise == "q":
        break
    intuserChoise = int(userChoise)
    compChoise = random.randint(0,2)
    print(f"Выбор компьютера {compChoise}")

    if intuserChoise == compChoise:
        print("Ничья")
        userScore+=0.5
        compScore += 0.5
        print(f'Очки пользователя {userScore}')
        print(f'Очки компа {compScore}')
    elif intuserChoise == 0 and compChoise == 2:
        print("Пользователь победил")
        userScore+=1
        print(f'Очки пользователя {userScore}')
        print(f'Очки компа {compScore}')
    elif compChoise > intuserChoise:
        print("Победил компьютер")
        compChoise+=1
        print(f'Очки пользователя {userScore}')
        print(f'Очки компа {compScore}')
    elif intuserChoise > compChoise:
        print("Победил пользователь")
        userScore+=1
        print(f'Очки пользователя {userScore}')
        print(f'Очки компа {compScore}')
