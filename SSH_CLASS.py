#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import pexpect.pxssh
import optparse

class Client:
    def __init__(self, host, user, password):
        self.host=host
        self.user=user
        self.password=password
        self.session=self.connect()

    def connect(self):
        try:
            s=pexpect.pxssh.pxssh()
            s.login(self.host, self.user, self.password)
            return s

        except Exception, e:
            print e
            print '[-] Error Connecting'

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

if __name__ == '__main__':
    c=Client('localhost', '박성진', 'Sj199402')
    print c.send_command('ls')
