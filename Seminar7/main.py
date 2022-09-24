# Иванов Иван +712345
# Семенов Семен +734567
# Матвеев Матвей +756789
# Сидоров Дмитрий +712377
# Григорьев Станислав +799875
# Разделим сервис на этапы:
# Как можно вводить данные?
# ‘Фамилия Имя Номер’
# Как их обрабатывать? Где хранить?
# user = {‘Name’:’’, ‘Last Name’:’’, ‘number’:’’ }
# user_list = [user1,user2,user3……]
# Как запрашивать и получать данные?
# Какие функции можно для этого создать?
# Как вынести функции в модули?
import csv

user_list = []


def data_input():
    #global user_list
    count = int(input('Сколько человек Вы хотите ввести в справочник: '))
    user = {'Last Name': '', 'Name': '', 'Number': ''}
    for i in range(count):
        text = input('Введите имя, фамилию, телефон через пробел: ').split()
        user_list.append(dict(zip(user, text)))

    with open('users.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f, fieldnames=list(user_list[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in user_list:
            writer.writerow(d)
    print(user_list)

def ask_key():
    #global user_list
    item = input('Введите искомое: ')
    temp_list = []
    with open('users.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if item in row:
                print(f'Фамилия: {row[0]}, Имя: {row[1]}, tel: {row[2]}')
    # key = input('Введите искомое: ')
    # for item in temp_list:
    #     for data in item.values():
    #         if key == data:
    #             print(item)

#data_input()
ask_key()