'''
Created on 2009-9-11

@author: selfimpr
'''
class Table(object):
    def __init__(self, *columns):
        self.datas = {}
        self.heads = []
        self.count = 0
        for column in columns:
            self.heads.append(column)
            self.datas.update({column: []})
    def add_column(self, *columns):
        for column in columns:
            self.heads.append(column)
            self.datas.update({column: ["" for i in range(self.count)]})
    def get_heads(self):
        return self.heads
    def insert(self, **values):
        for column in self.heads:
            if column in values:
                self.datas[column].append(values[column])
            else:
                self.datas[column].append("")
        self.count += 1
    def print_datas(self):
        for head in self.heads:
            print head.ljust(19), "|",
        print
        print "---------------------------------------------------------------------"
        for i in range(self.count):
            for head in self.heads:
                if head in self.datas:
                    print self.datas[head][i].ljust(19), "|",
            print


a = Table("username", "password")
a.add_column("name")
a.insert(username = "admin", password = "admin", name = "Jatty")
a.insert(username = "administrator", password = "administrator", name = "Jatty")
a.insert(username = "selfimpr", password = "selfimpr", name = "Jatty")
a.insert(username = "manager", password = "manager", name = "Jatty")
a.add_column("create_time")
a.insert(username = "guest", name = "Jatty")
a.print_datas()