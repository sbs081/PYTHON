'''
Created on 2009-9-11

@author: selfimpr
'''
import datetime, hashlib

class Information(object):
    def __init__(self, password, last_login_timestamp):
        self.password = password
        self.last_login_timestamp = last_login_timestamp
    def modify_password(self, new_password):
        self.password = new_password
    def modify_timestamp(self, last_login_timestamp):
        self.last_login_timestamp = last_login_timestamp
    def get_password(self):
        return self.password
    def get_last_login_timestamp(self):
        return self.last_login_timestamp
users = {}
users_file = open('users.data', 'r')
for line in users_file.readlines():
    properties = line.split("`")
    users[properties[0]] = Information(properties[1], properties[2])
users_file.close() 

def register(username, password):
    if username in users:
        return False
    users[username] = Information(str(hashlib.md5(password).hexdigest()), datetime.datetime.now())
    users_file = open('users.data', 'a+')
    print >> users_file, username + "`" + str(hashlib.md5(password).hexdigest()) + "`" + \
                     str(users[username].get_last_login_timestamp())
    users_file.close()
    return True

def check(username, password):
    password = str(hashlib.md5(password).hexdigest())
    return username in users and password == users[username].get_password()

def get_command():
    command = raw_input('''
    enter a command
    -------------------------------------
    register | entry register system
    login    | entry login system
    view     | view all the users
    del      | delete a user from system
    exit     | exit our system
    ''')
    while command.strip() not in ['register', 'login', 'exit', 'view', 'del']:
        command = raw_input('''
        enter a command
        -------------------------------------
        register | entry register system
        login    | entry login system
        view     | view all the users
        del      | delete a user from system
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
            username = get_username()
            password = get_password()
            while keeploop and not check(username, password):
                print "login lose, username or password error!"
                username = get_username()
                password = get_password()
                if i >= 2:
                    print "you tried three times, please try later!"
                    keeploop = False
                i += 1
            if keeploop:
                print "congratulations, you are login success!"
                now = datetime.datetime.now()
                user_info = users[username]
                last_login = user_info.get_last_login_timestamp()
                if now.date() == last_login.date() \
                and now.hour - last_login.hour < 4:
                    print 'You already logged in at:', str(last_login)
                user_info.modify_timestamp(datetime.datetime.now())
        elif command == 'view':
            print '''
            username             |password              |lastlogin
            ------------------------------------------------------------------------'''
            for user in users:
                print '            ' + user.ljust(20), \
                '|', \
                users[user].get_password().ljust(20), \
                '|', \
                str(users[user].get_last_login_timestamp()).ljust(20)
        elif command == 'del':
            username = get_username()
            if username not in users:
                print 'You enterd username not exist'
            else:
                del users[username]
                print 'user was deleted whose name is ' + username
        command = get_command()