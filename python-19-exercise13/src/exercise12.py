'''
Created on 2009-10-7

@author: selfimpr
'''

class Message(object):
    def __init__(self, publisher, msg = '', receiver = None):
        self.publisher = publisher
        self.msg = msg
        self.receivers = receiver if receiver else None

class User(object):
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

class Room(object):
    def __init__(self, users):
        self.users = {}
        if isinstance(users, list):
            for user in users:
                self.users[user.username] = user
        elif isinstance(users, User):
            self.users[users.username] = users
    
    def join(self, user):
        self.users.append(user)
    
    def exit(self, username):
        self.users.pop(username)

if __name__ == '__main__':
    pass