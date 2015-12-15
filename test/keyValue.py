__author__ = 'joe'
my_dict = {'john':372789838, 'mike':32378,'tom':237288}
print my_dict['john']
print 'job' in my_dict
my_dict['job'] = 372783888
print 'job' in my_dict

for name in my_dict:
    print name
print my_dict.items()
print my_dict.values()
print my_dict.keys()
print len(my_dict)

# name = raw_input('please enter your name:')
# print 'hello ', name

print ord('a')
print chr(65)
print u'A'.encode('utf-8')