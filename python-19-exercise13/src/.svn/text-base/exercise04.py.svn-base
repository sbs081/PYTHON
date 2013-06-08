'''
Created on 2009-10-4

@author: selfimpr
'''

class DB(object):
    def __init__(self):
        self.data = {}
        f = open('c:\\users.txt', 'r')
        for line in f:
            d = line.split(':')
            self.data[d[0]] = {'username': d[0], 'password': d[1], 'isNew': False}
        f.close()
    def register(self, username, password):
        if username in self.data:
            print 'username exist!'
            return 
        self.data[username] = {'username': username, 'password': password, 'isNew': True}
    def login(self, username, password):
        return username in self.data and password == self.data[username]['password']
    def modify(self, username, oldpassword, newpassword):
        if username in self.data and oldpassword == self.data[username]['password']:
            self.data[username]['password'] = newpassword
        else:
            print 'please provide availability password'
    def __del__(self):
        f = open('c:\\users.txt', 'w')
        f.writelines('%s:%s\n' % (user['username'], user['password']) for user in self.data.values())
        f.close()

if __name__ == '__main__':
    db = DB()
    db.register('selfimpr', '2a')
    db.register('admin', 'admin')
    db.login('selfimpr', '2a0d1q22f9')
    db.modify('admin', 'admin', '2a0d1q22f9')
    