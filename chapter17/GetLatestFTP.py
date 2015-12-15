__author__ = 'joe'
# !/usr/bin/env python

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except(socket.error, socket.gaierror), e:
        print 'ERROR: cannot reach "%s"' % HOST
    return
    print '*** connected to host "%s"' % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
    q.quit()
    return
    print '*** logged in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' % DIRN
    q.quit()
    return
    print '*** changed to "%s" folder' % DIRN

    try:
        f.retrbinary('RETR %s' %FILE, open(FILE, 'wb').write())
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CWD' % FILE
        q.quit
        return

if __name__ == "__main__":
    main()
