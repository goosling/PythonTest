__author__ = 'joe'

class MyClass(object):
    myVersion = '1.1'
    def showMyVersion(self):
        print self.myVersion
mc = MyClass
print mc.myVersion
print type(mc)
print dir(MyClass)
print MyClass.__dict__

L1 = [1,2,3,4]
L2 = L1
L1[0] = 5
print L1,L2
a = 5
b = a
a = 4
print a , b