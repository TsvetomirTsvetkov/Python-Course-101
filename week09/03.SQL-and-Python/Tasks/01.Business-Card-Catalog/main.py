# main.py

import sqlite3


def create_users_table():
    connection = sqlite3.connect("business.db")
    cursor = connection.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
        full_name VARCHAR(100) NOT NULL,
        email VARCHAR(62) NOT NULL,
        age INTEGER NOT NULL,
        phone VARCHAR(15) NOT NULL,
        additional_info TEXT
    )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def help():
    print('#############\n###Options###\n#############')
    print('1. `add` - insert new business card')
    print('2. `list` - list all business cards')
    print('3. `delete` - delete a certain business card (`ID` is required)')
    print('4. `get` - display full information for a certain business card (`ID` is required)')
    print('5. `help` - list all available options')


def add():
    full_name = input('Enter user name: ')
    email = input('Enter email: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    additional_info = input('Enter addional info (optional): ')

    connection = sqlite3.connect("business.db")
    cursor = connection.cursor()
    query = '''
        INSERT INTO User (full_name, email, age, phone, additional_info)
            VALUES (?, ?, ?, ?, ?)
    '''
    cursor.execute(query, (full_name, email, age, phone, additional_info))
    connection.commit()
    connection.close()


def list_users():
    print('##############\n###Contacts###\n##############')
    connection = sqlite3.connect("business.db")
    cursor = connection.cursor()
    query = '''
        SELECT id, email, full_name FROM User
    '''
    cursor.execute(query)
    list_of_users = cursor.fetchall()

    counter = 1
    for user in list_of_users:
        print(f'{counter}. ID: {user[0]}, Email: {user[1]}, Full name: {user[2]}')
        counter += 1

    connection.commit()
    connection.close()


def get():
    user_id = input('Enter id: ')

    connection = sqlite3.connect("business.db")
    cursor = connection.cursor()
    query = f'''
        SELECT * FROM User WHERE id == {user_id}
    '''
    cursor.execute(query)

    user = cursor.fetchone()
    if user is None:
        print(f'No user found with id == {user_id}.')
    else:
        print('\nContact info:\n')
        print_details(user)

    connection.commit()
    connection.close()


def delete():
    user_id = input('Enter id: ')

    connection = sqlite3.connect("business.db")
    cursor = connection.cursor()
    query = f'''
        SELECT * FROM User WHERE id == {user_id}
    '''
    cursor.execute(query)
    user = cursor.fetchone()

    if user is None:
        print(f'No user found with id == {user_id}.')
    else:
        print('Following contact is deleted successfully:\n')
        print_details(user)

    query = f'''
        DELETE FROM User WHERE id == {user_id}
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def print_details(user):
    print('###############')
    print(f'Id: {user[0]}')
    print(f'Full name: {user[1]}')
    print(f'Email: {user[2]}')
    print(f'Age: {user[3]}')
    print(f'Phone: {user[4]}')
    print(f'Additional info: {user[5]}')
    print('###############')


def main():
    create_users_table()
    print(
        'Hello! This is your business card catalog. What would you like? (enter "help" to list all available options)'
    )

    while True:
        command = input('Enter command: ')

        if command == 'help':
            help()
        elif command == 'add':
            add()
        elif command == 'list':
            list_users()
        elif command == 'get':
            get()
        elif command == 'delete':
            delete()
        else:
            print('Unrecognized command. Try again!')


if __name__ == '__main__':
    main()
