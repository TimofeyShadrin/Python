import view_all as va


def ask():
    text = input('Введите фамилию участника scrum-команды\n'
                 'или нажмите Enter, чтобы просмотреть всех: ')
    if text.isalpha() and text != '':
        va.view_all(text)
        if len(va.all_list) == 0:
            print('Сотрудник с такой фамилией не найден!')
        va.all_list.clear()
    elif text == '':
        va.view_all()
        va.all_list.clear()
    else:
        print('Проверьте Ваш ввод!')


def menu():
    answer = 'д'
    while True:
        if answer == 'д':
            ask()
            try:
                answer = input('Повторить поиск? Введите: да или любой символ для выхода! ').lower()[0]
            except:
                break
        else:
            break



