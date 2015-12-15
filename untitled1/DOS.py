__author__ = 'joe'

import os
def cmdDIR():
    dirName = os.getcwd()
    for i in os.listdir(dirName):
        print dirName+'\\'+i
def cmdMore(cmd):
    print cmd.split(" ")
    fileName = cmd.split(" ")[1]
    with open(fileName) as fobj:
        for line in fobj:
            print line
def cmdType(cmd):
    fileName = cmd.split(" ")[1]
    type(fileName)
def cmdCopy(cmd):
    oldFile = cmd.split(" ")[1]
    newFile = cmd.split(" ")[2]
    with open(oldFile, 'r') as foldObj:
        with open(newFile, 'w') as fnewObj:
            for line in foldObj:
                fnewObj.write(line)
def cmdRen(cmd):
    cmdCopy(cmd)
    delFile = cmd.split(" ")[1]
    os.remove(delFile)

def DOS():
    while True:
        cmd = raw_input("-->")
        if cmd.find("ls") != -1:
            cmdDIR()
        elif cmd.find("more") != -1:
            cmdMore(cmd)
        elif cmd.find("cat") != -1:
            cmdType(cmd)
        elif cmd.find("cp") != -1:
            cmdCopy(cmd)
        elif cmd.find("mv") != -1:
            cmdRen(cmd)
        else:
            print "sorry, command is wrong! Please enter again"
if __name__ == "__main__":
    DOS()