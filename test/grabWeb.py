__author__ = 'joe'
#!/usr/bin/env python

from urllib import urlretrieve



def firstNonBlank(lines):
    for eachline in lines:
        if not eachline.strip():
            continue
        else:
            return eachline

def firstLast(webPage):
    f = open(webPage)
    lines = f.readline()
    f.close()
    print firstNonBlank()
    lines.reverse()
    print firstNonBlank()

def download(url = 'http://www', process = firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None

    if retval:
        process(retval)

if __name__ == '__main__':
    download()

