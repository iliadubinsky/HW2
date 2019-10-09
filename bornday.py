# Год и день рождения А.С.Пушкина
year_of_birth = input('What is Alexander Pushkin year of birth?  ')
year_of_birth = int(year_of_birth)
if year_of_birth == 1799:
    print('Great! Correct year!')
    date_of_birth = input('What is Alexander Pushkin date of birth?  ')
    if date_of_birth == 'June 6' or '6 of June' or '6 June' or '6 июня'or 'june 6' or '6 of june' or '6 june':
        print('Great! You are right! Alexander Pushkin was born on June 6, 1799')
    else:
        print('Wrong date!')
else:
    print('No, wrong year!')
