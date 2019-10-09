# спрашивает год рождения А.С.Пушкина и продолжает спрашивать до верного ответа

age = input('What is Alexander Pushkin year of birth?  ')
age = int(age)
while not age == 1799:
    print('Incorrect year! Try again: ')
    age = input('What is Alexander Pushkin year of birth?  ')
    age = int(age)
print('Congratulations, you are right! Pushkin birth year is', age)
