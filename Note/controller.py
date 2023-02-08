import note

atr_of_note = {'id': '',
               'Added': '',
               'Title': '',
               'Body': ''}

list_of_notes = []


def view():
    print('Commands:\n'
          '   add - add note,\n'
          '   list - view all notes,\n'
          '   exit')
    while True:
        choose = input('Please enter the command: ')
        if choose == 'add':
            title = input('Please enter the title: ')
            body = input('Please enter the message: ')
            object_note = note.Note(title, body)
            list_of_notes.append(dict(zip(atr_of_note, [object_note.get_id(),
                                                        str(object_note.get_create_date()),
                                                        object_note.get_title(),
                                                        object_note.get_text()])))
        elif choose == 'list':
            for your_note in list_of_notes:
                print(your_note)
        elif choose == 'exit':
            print('Good bye')
            break
        else:
            print('Your input is incorrect')
