from scrum import read_contacts as rc
from scrum import read_status as rs
from scrum import read_post as rp
from scrum import del_record as dr


def find_menu():
    while True:
        print('1. View employee contacts\n'
              '2. View employee statuses\n'
              '3. View the employee\'s position\n'
              '4. Delete record\n'
              '5. Main menu')
        try:
            answer = int(input('Please enter the item number: '))
            if answer == 1:
                rc.read_contacts()
                break
            elif answer == 2:
                rs.read_status()
                break
            elif answer == 3:
                rp.read_post()
                break
            elif answer == 4:
                dr.del_record()
                break
            elif answer == 5:
                break
            else:
                print('Your input is incorrect!')
        except:
            print('Your input is incorrect!')