# программа спрашивает у пользователя год рождения А.С.Пушкина и реагирует на результат
age = input('What is Alexander Pushkin year of birth?  ')
age = int(age)
if age == 1799:
    print('Верно - Congratulations, you are right!')
else:
    print('Неверно - You are wrong! Go look for the right answer.')

