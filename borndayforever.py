# Спрашиваем год рождения Пушкина до правильного ответа, после спрашиваем день рождения до правильного ответа.

year_of_birth = input('What is Alexander Pushkin year of birth?  ')
year_of_birth = int(year_of_birth)
while not year_of_birth == 1799:
    print('Incorrect! Try one more time!')
    year_of_birth = input('What is Alexander Pushkin year of birth?  ')
    year_of_birth = int(year_of_birth)
print('Correct year!')
date_of_birth = input('On what day in June was Alexander Pushkin born?  ')
while not date_of_birth == 'June 6':
    print('Incorrect! Try one more time!')
    date_of_birth = input('What is Alexander Pushkin date of birth?  ')
print('Great! You are right! Alexander Pushkin was born on June 6, 1799')
