from scrum import read_contacts as rc


def find_menu():
    while True:
        print('1. View employee contacts\n'
              '2. View employee statuses\n'
              '3. View the employee\'s position\n'
              '4. Main menu')
        try:
            answer = int(input('Please enter the item number: '))
            if answer == 1:
                rc.read_contacts()
                break
            elif answer == 2:
                break
            elif answer == 3:
                break
            elif answer == 4:
                break
            else:
                print('Your input is incorrect!')
        except:
            print('Your input is incorrect!')