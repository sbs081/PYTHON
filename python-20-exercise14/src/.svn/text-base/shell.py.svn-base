'''
Created on 2009-10-21

@author: selfimpr
@blog: http://blog.csdn.net/lgg201
@E-mail: lgg860911@yahoo.com.cn
'''

from sys import stdout
from subprocess import Popen, PIPE

def pipecmd(cmdstr):
    if isinstance(cmdstr, str): # estimate if the argument is string
        cmds = cmdstr.split('|') # split intact cmdstr to sigle command
        cmds = [cmd.strip() for cmd in cmds] # strip space character
        length = len(cmds)
        popens = []
        for index, cmd in enumerate(cmds): # each all the commands
            cmd_args = cmd.split(' ')
            cmd_args = [arg.strip() for arg in cmd_args]
            try:
                #################
                # get all the instance of Popen
                #################
                popens.append(eval('Popen(cmd_args%(stdin)s%(stdout)s)' % \
                               {'stdin': '' if index == 0 else ', stdin=PIPE', \
                                'stdout': ', stdout=stdout' if index == length - 1 else ', stdout=PIPE'}))
            except OSError, e:
                print 'arises os error'
        #################
        # process pipe
        #################
        prev = None
        for index, popenobj in enumerate(popens):
            if not prev:
                prev = popenobj
                continue
            popenobj.stdin.write(prev.stdout.read())
            prev = popenobj

if __name__ == '__main__':
    print pipecmd('dir c:\\ | more')