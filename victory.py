# Викторина -- даты рождения известных людей

while True:
    date_pushkin = input('Введите год рождения Пушкина')
    # год рождения Пушкина - 1799
    date_gogol = input('Введите год рождения Гоголя')
    # год рождения Гоголя - 1809
    date_tolstoy = input('Введите год рождения Толстого')
    # год рождения Толстого - 1828
    date_dostoevsky = input('Введите год рождения Достоевского')
    # год рождения Достоевского - 1821
    date_bulgakov = input('Введите год рождения Булгакова')
    # год рождения Булгакова - 1891

    right_answer = 0
    if date_pushkin == '1799':
        right_answer = right_answer + 1
    else:
        right_answer = right_answer
    if date_gogol == '1809':
        right_answer = right_answer + 1
    else:
        right_answer = right_answer
    if date_tolstoy == '1828':
        right_answer = right_answer + 1
    else:
        right_answer = right_answer
    if date_dostoevsky == '1821':
        right_answer = right_answer + 1
    else:
        right_answer = right_answer
    if date_bulgakov == '1891':
        right_answer = right_answer + 1
    else:
        right_answer = right_answer

    print('Количество правильных ответов:', right_answer )
    print('Количество ошибочных ответов:', 5-right_answer )
    print('Процент правильных ответов:', right_answer*100/5 )
    print('Процент ошибочных ответов:', (5-right_answer)*100/5 )

    answer = input('Хотите сыграть еще раз?')
    if answer == 'нет':
        print('Cпасибо за игру')
        break
    print('Начинаем сначала!')