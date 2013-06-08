'''
Created on 2009-9-11

@author: selfimpr
'''

users = {}

def register(username, password):
    if username in users:
        return False
    users[username] = password
    return True

def check(username, password):
    return username in users and password == users[username]

def get_command():
    command = raw_input('''
    enter a command
    --------------------------------
    register | entry register system
    login    | entry login system
    exit     | exit our system
    ''')
    if command not in ['register', 'login', 'exit']:
        command = raw_input('''
        enter a command
        --------------------------------
        register | entry register system
        login    | entry login system
        exit     | exit our system
        ''')
    return command

def get_username():
    return raw_input("Please enter your username: \n")
def get_password():
    return raw_input("Please enter your password: \n")

if __name__ == '__main__':
    command = get_command()
    while command != "exit":
        if command == "register":
            while not register(get_username(), get_password()):
                print "usernmae exist!"
            print "congratulations, you are register success!"
        elif command == "login":
            i = 0
            keeploop = True
            while keeploop and not check(get_username(), get_password()):
                print "login lose, username or password error!"
                if i >= 2:
                    print "you tried three times, please try later!"
                    keeploop = False
                i += 1
            if keeploop:
                print "congratulations, you are login success!\nwelcome to our system!"
        command = get_command()