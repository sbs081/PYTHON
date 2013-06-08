'''
Created on 2009-10-7

@author: selfimpr
'''

import re, sys, os

class Shell(object):
    _commands = {'dir': 'dir', 
                 'more': 'more', 
                 'cat': 'type', 
                 'cp': 'copy', 
                 'mv': 'move', 
                 'rm': 'rmdir'}
    _public_regular = re.compile('^[ \t]*(dir|more|cat|cp|mv|rm|q)[ \t]*(.*)')
    _supportCommands = [command for command in _commands.keys()]
    
    def __init__(self):
        Shell._supportCommands.append('q')
        self.flag = True
    
    def run(self):
        while self.flag:
            command_tuple = self.parseCommand(self.getCommand())
            if command_tuple:
                self.execute(command_tuple)
    
    def execute(self, command_tuple):
        os.system('%s %s' % command_tuple)
    
    def parseCommand(self, command):
        m = Shell._public_regular.match(command)
        if not m:
            raise Exception, 'Your input error.'
        if m.group(1) == 'q':
            self.flag = False
            return None
        command = Shell._commands[m.group(1)]
        args = m.group(2)
        return command, args
        
    
    def getCommand(self):
        command = self._command_input()
        while Shell._public_regular.match(command).group(1) not in Shell._supportCommands:
            command = self._command_input()
        return command 
    
    def _command_input(self):
        return raw_input('''
                support command:
                 command |  mean
                ------------------------------------------
                  dir    | list specify directory
                  more   | pagination display
                  cat    | type a file into window
                  cp     | copy a file to other directory
                  mv     | move a file to other directory
                  rm     | delete a file or directory
                  q      | exit
                ''')
    

if __name__ == '__main__':
    shell = Shell()
    shell.run()