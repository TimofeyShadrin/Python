from scrum.find import find_menu as fm
from scrum import create_record as cr
from scrum.find import find_worker as fw


def repeat_find():
    while True:
        phrase = input('\nPlease enter phrase in data of employee: ')
        fw.find_worker(phrase)
        if len(fw.all_list) != 0:
            break
        else:
            print('The search yielded no results!\n\n'
                  '1. Repeat search?\n'
                  '2. Main menu')
            try:
                look = int(input('Please enter the item number: '))
                if look == 1:
                    continue
                elif look == 2:
                    break
                else:
                    print('Your input is incorrect!')
            except:
                print('Your input is incorrect!')


def menu():
    while True:
        print('\nMain menu:\n'
              '1. Create record\n'
              '2. Find employee\n'
              '3. Exit\n')
        try:
            choice = int(input('Please enter the item number of main menu: '))
            if choice == 1:
                cr.create_record()
            elif choice == 2:
                repeat_find()
                fm.find_menu()
                fw.all_list.clear()
                fw.serial.clear()
            elif choice == 3:
                break
            else:
                print('Your input is incorrect!')
        except:
            print('Your input is incorrect!')
