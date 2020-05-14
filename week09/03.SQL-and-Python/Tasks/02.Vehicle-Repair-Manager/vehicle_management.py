# vehicle_management.py

import sqlite3


def create_base_user():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS BaseUser (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            user_name VARCHAR(100) NOT NULL UNIQUE,
            email VARCHAR(62) NOT NULL UNIQUE,
            phone INTEGER NOT NULL,
            address VARCHAR(100) NOT NULL
        )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_client():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS Client (
            base_id INTEGER NOT NULL,
            FOREIGN KEY(base_id) REFERENCES BaseUser(id)
        )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_mechanic():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS Mechanic (
            base_id INTEGER NOT NULL,
            title VARCHAR(50),
            FOREIGN KEY(base_id) REFERENCES BaseUser(id)
        )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_service():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS Service (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            name VARCHAR(50)
        )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_mechanic_service():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS MechanicService (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            mechanic_id INTEGER,
            service_id INTEGER,
            FOREIGN KEY(mechanic_id) REFERENCES Mechanic(base_id),
            FOREIGN KEY(service_id) REFERENCES Service(id)
        )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_vehicle():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS Vehicle (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            category VARCHAR(50),
            make VARCHAR(50),
            model VARCHAR(50),
            register_number VARCHAR(10),
            gearbox VARCHAR(20),
            owner INTEGER,
            FOREIGN KEY(owner) REFERENCES Client(base_id)
        )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_repair_hour():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
        CREATE TABLE IF NOT EXISTS RepairHour (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            date VARCHAR(8),
            start_hour VARCHAR(4),
            vehicle INTEGER,
            bill REAL,
            mechanic_service INTEGER,
            FOREIGN KEY(vehicle) REFERENCES Vehicle(id),
            FOREIGN KEY(mechanic_service) REFERENCES MechanicService(id)
        )
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def create_tables():
    create_base_user()
    create_client()
    create_mechanic()
    create_service()
    create_mechanic_service()
    create_vehicle()
    create_repair_hour()


def check_user(user):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = f'''
       SELECT *
       FROM BaseUser
       LEFT OUTER JOIN Client
       ON BaseUser.id == Client.base_id
       LEFT OUTER JOIN Mechanic
       ON BaseUser.id == Mechanic.base_id
       WHERE BaseUser.user_name = '{user}'
    '''
    cursor.execute(query)

    found_user = cursor.fetchall()

    connection.commit()
    connection.close()

    return found_user


def create_user():
    user_type = input('Are you a Client or Mechanic?\n')
    user_name = input('Provide user_name:\n')
    phone = input('Provide phone_number:\n')
    email = input('Provide email:\n')
    address = input('Provide address:\n')

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
        INSERT INTO BaseUser(user_name, email, phone, address)
        VALUES(?, ?, ?, ?)
    '''
    cursor.execute(query, (user_name, email, phone, address))
    if user_type == 'Mechanic':
        query = f'''
            INSERT INTO Mechanic(base_id, title)
            VALUES((SELECT id FROM BaseUser WHERE user_name = '{user_name}'), "Mechanic")
        '''
        cursor = connection.cursor()
        cursor.execute(query)
    elif user_type == 'Client':
        query = f'''
            INSERT INTO Client(base_id)
            VALUES((SELECT id FROM BaseUser WHERE user_name = '{user_name}'))
        '''
        cursor = connection.cursor()
        cursor.execute(query)

    connection.commit()
    connection.close()

    print(
        f'Thank you, {user_name}!\nWelcome to Vehicle Services!\nNext time you try to login, provide your user_name!\n'
    )


def fill_repair_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = '''
        SELECT *
        FROM RepairHour
        WHERE (date = "24-05-2020" AND start_hour = "10:00") OR
        (date = "25-05-2020" AND start_hour = "16:00") OR
        (date = "27-05-2020" AND start_hour = "11:20")
    '''
    cursor.execute(query)
    list_of_hours = cursor.fetchall()
    if list_of_hours == []:
        query = '''
            INSERT INTO RepairHour(date, start_hour)
            VALUES ("24-05-2020", "10:00"),
            ("24-05-2020", "10:40"),
            ("25-05-2020", "16:00"),
            ("27-05-2020", "11:20")
        '''
    cursor.execute(query)
    connection.commit()
    connection.close()


def print_commands_client():
    print('list_all_free_hours')  # SAME
    print('list_free_hours <date>')  # SAME
    print('save_repair_hour <hour_id>')
    print('update_repair_hour <hour_id>')
    print('delete_repair_hour <hour_id>')
    print('add_vehicle')
    print('update_vehicle <vehicle_id>')
    print('delete_vehicle <vehicle_id>')
    print('exit\n')  # SAME


def print_commands_mechanic():
    print('list_all_free_hours')  # SAME
    print('list_free_hours <date>')  # SAME
    print('list_all_busy_hours')
    print('list_busy_hours <date>')
    print('add_new_repair_hour')
    print('add_new_service')
    print('update_repair_hour <hour_id>')
    print('exit\n')

# Commands Client


def list_all_free_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = f'''
       SELECT *
       FROM RepairHour
       WHERE vehicle IS NULL AND mechanic_service IS NULL
    '''
    cursor.execute(query)

    free_hours = cursor.fetchall()

    connection.commit()
    connection.close()

    print('+----+-------------+-------+')
    print('| id | date | start_hour   |')
    print('+----+---------------------+')
    for elem in free_hours:
        print('|', elem[0], ' ' * (1 - len(str(elem[0]))), '|', elem[1], '| ', elem[2], '|')
    print('+----+---------------------+')


def list_free_hours(date):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = f'''
       SELECT *
       FROM RepairHour
       WHERE date = '{date}'
    '''
    cursor.execute(query)

    free_hours = cursor.fetchall()

    connection.commit()
    connection.close()

    print('+----+-------------+-------+')
    print('| id | date | start_hour   |')
    print('+----+---------------------+')
    for elem in free_hours:
        print('|', elem[0], ' ' * (1 - len(str(elem[0]))), '|', elem[1], '| ', elem[2], '|')
    print('+----+---------------------+')


def list_all_busy_hours():
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = f'''
       SELECT *
       FROM RepairHour
       WHERE vehicle IS NOT NULL AND mechanic_service IS NOT NULL
    '''
    cursor.execute(query)

    free_hours = cursor.fetchall()

    connection.commit()
    connection.close()

    print('+----+-------------+-------+')
    print('| id | date | start_hour   |')
    print('+----+---------------------+')
    for elem in free_hours:
        print('|', elem[0], ' ' * (1 - len(str(elem[0]))), '|', elem[1], '| ', elem[2], '|')
    print('+----+---------------------+')


def list_busy_hours(date):
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()

    query = f'''
       SELECT *
       FROM RepairHour
       WHERE vehicle IS NOT NULL AND mechanic_service IS NOT NULL AND date = '{date}'
    '''
    cursor.execute(query)

    free_hours = cursor.fetchall()

    connection.commit()
    connection.close()

    print('+----+-------------+-------+')
    print('| id | date | start_hour   |')
    print('+----+---------------------+')
    for elem in free_hours:
        print('|', elem[0], ' ' * (1 - len(str(elem[0]))), '|', elem[1], '| ', elem[2], '|')
    print('+----+---------------------+')


def add_vehicle(owner):
    category = input('Vehicle category: ')
    make = input('Vehicle make: ')
    model = input('Vehicle model: ')
    register_number = input('Vehicle register number: ')
    gearbox = input('Vehicle gear box: ')
    print()

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = f'''
       INSERT INTO Vehicle(category, make, model, register_number, gearbox, owner)
       VALUES(?, ?, ?, ?, ?, (SELECT * FROM Client WHERE base_id = '{owner[0][0]}'))
    '''
    cursor.execute(query, (category, make, model, register_number, gearbox))
    connection.commit()
    connection.close()

    print('Thank you! You added new personal vehicle!\n')


def delete_vehicle(delete_id):
    print()
    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = f'''
       DELETE FROM Vehicle
       WHERE id = '{delete_id}'
    '''
    cursor.execute(query)
    connection.commit()
    connection.close()

    print(f'Vehicle with id = {delete_id} has been deleted! (If it was in the table)\n')


def update_vehicle(owner, vehicle_id):
    category = input('Update vehicle category: ')
    make = input('Update vehicle make: ')
    model = input('Update vehicle model: ')
    register_number = input('Update vehicle register number: ')
    gearbox = input('Update vehicle gear box: ')
    print()

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = f'''
       UPDATE Vehicle
       SET category = ?, make = ?, model = ?, register_number = ?, gearbox = ?
       WHERE id = {vehicle_id} AND owner = {owner[0][0]}
    '''
    cursor.execute(query, (category, make, model, register_number, gearbox))
    connection.commit()
    connection.close()

    print(f'Vehicle with id = {vehicle_id} has been updated.\n')


def add_new_service():
    new_service = input('Provide New service name: ')

    connection = sqlite3.connect('vehicle_management.db')
    cursor = connection.cursor()
    query = f'''
       INSERT INTO Service(name)
       VALUES (?)
    '''
    cursor.execute(query, (new_service))
    connection.commit()
    connection.close()


def execute_command(user, user_type, command):
    command_list = command.split()

    commands = {
        "Client": [
            "list_all_free_hours",  # DONE
            "list_free_hours",  # DONE
            "save_repair_hour",
            "update_repair_hour",
            "delete_repair_hour",
            "add_vehicle",  # DONE
            "update_vehicle",  # DONE
            "delete_vehicle"],  # DONE
        "Mechanic": [
            "list_all_free_hours",  # DONE
            "list_free_hours",  # DONE
            "list_all_busy_hours",  # DONE
            "list_busy_hours",  # DONE
            "add_new_repair_hour",
            "add_new_service",  # NOT WORKING
            "update_repair_hour"
        ]}

    if user_type == "Client" and command_list[0] in commands[user_type]:
        if command_list[0] == "list_all_free_hours":
            list_all_free_hours()
        elif command_list[0] == "list_free_hours":
            list_free_hours(command_list[1])
        elif command_list[0] == "add_vehicle":
            add_vehicle(user)
        elif command_list[0] == "delete_vehicle":
            delete_vehicle(command_list[1])
        elif command_list[0] == "update_vehicle":
            update_vehicle(user, command_list[1])
    elif user_type == "Mechanic" and command_list[0] in commands[user_type]:
        if command_list[0] == "list_all_free_hours":
            list_all_free_hours()
        elif command_list[0] == "list_free_hours":
            list_free_hours(command_list[1])
        elif command_list[0] == "list_all_busy_hours":
            list_all_busy_hours()
        elif command_list[0] == "list_busy_hours":
            list_busy_hours(command_list[1])
        elif command_list[0] == "add_new_service":
            add_new_service()
    else:
        print('Unrecognized command. Try again!')


def main():
    create_tables()
    fill_repair_hours()

    user = input('Hello!\nProvide user name: ')
    print()

    found_user = check_user(user)

    working = True

    if found_user == []:
        while True:
            answer = input('Unknown user!\nWould you like to create new user?\n')
            agree = ['yes', 'y']
            disagree = ['no', 'n']

            if answer.lower() in agree:
                create_user()
                break
            elif answer.lower() in disagree:
                print('Goodbye!\n')
                working = False
                break
            else:
                print('Unrecognized input! Try again!\n')

    while working:
        if found_user == []:
            found_user = check_user(user)
        else:
            print(f'Hello, {found_user[0][1]}!')
        print('You can choose from the following commands:\n')
        if found_user[0][5] is not None:
            print_commands_client()
            user_type = "Client"
        else:
            print_commands_mechanic()
            user_type = "Mechanic"

        command = input('>')
        if command == 'exit':
            print('Goodbye!')
            working = False
        else:
            execute_command(found_user, user_type, command)


if __name__ == '__main__':
    main()
