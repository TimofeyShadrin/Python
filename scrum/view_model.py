import view_all as va
import view_status as vs
import change_status as cs

answer = 4
def ask():
    global answer
    text = input('Введите фамилию участника scrum-команды целиком или несколько первых букв\n'
                 'или нажмите Enter, чтобы просмотреть всех: ')
    if text.isalpha() and text != '':
        va.view_all(text)
        if len(va.all_list) == 0:
            print('Сотрудник с такой фамилией не найден!')
            print('\n1. Повторить операцию поиска;\n'
                    '2. Выход из программы.\n')
            while True:
                try:
                    look = int(input('Введите номер выбранного пункта: '))
                    if look == 1:
                        answer = 4
                        break
                    elif look == 2:
                        answer = 3
                        break
                    else:
                        print('Ваш ввод не корректен!')
                except:
                    print('Ваш ввод не корректен!')
        else:
            va.all_list.clear()
            answer = 0

    elif text == '':
        va.view_all()
        va.all_list.clear()
    else:
        print('Проверьте Ваш ввод!')


def menu():
    global answer
    while True:
        if answer == 4:
            ask()
        elif answer == 0:
            print('\n1. Посмотреть статус сотрудника;\n'
                    '2. Изменить статус сотдрунка;\n'
                    '3. Выход из программы;\n'
                    '4. Повторить поиск.\n')
            try:
                answer = int(input('Введите номер выбранного пункта: '))
            except:
                print('Ваш ввод не корректен!')
                answer = 4

        elif answer == 1:
            text = input('Введите фамилию сотрудника: ')
            vs.view_status(text)
            print('\n1. Изменить статус сотдрунка;\n'
                  '2. Выход из программы.\n')
            try:
                look = int(input('Введите номер выбранного пункта: '))
                if look == 1:
                    answer = 2
                elif look == 2:
                    answer = 3
                else:
                    print('Ваш ввод не корректен!')
                    answer = 4
            except:
                print('Ваш ввод не корректен!')
                answer = 4
        elif answer == 2:
            try:
                id = int(input('Введите ID сотрундика, у которого изменяется статус: '))
                temp = str(input('Введите новый статус: '))
                cs.change_status(id, temp)
                print('\n1. Посмотреть статус сотрудника;\n'
                      '2. Выход из программы.\n')
                look = int(input('Введите номер выбранного пункта: '))
                if look == 1:
                    answer = 1
                elif look == 2:
                    answer = 3
                else:
                    print('Ваш ввод не корректен!')
                    answer = 4
            except:
                print('Ваш ввод не корректен!')
                answer = 4
        elif answer == 3:
            break
        else:
            answer = 0



