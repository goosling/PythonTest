__author__ = 'joe'

s = 'I am a String'
name = s + '\nname'
print name
print 'a' in s

def vowels_count(s):
    count = 0
    for c in s:
        if c in 'aeiouAEIOU':
            count += 1
    return count
print vowels_count('hello_world')

def selection_sort_v1(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1,len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst.insert(i, lst.pop(min_index))

def selection_sort_v2(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index] :
                min_index = j
        swap(lst, i, min_index)

def bubble_sort(lst):
    top = len(lst) - 1
    is_exchanged = True
    while is_exchanged:
        is_exchanged = False
        for i in range(top):
            if lst[i] > lst[i+1]:
                swap(lst,i,i+1)
        top -= 1

def swap(lst,a,b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp
    return lst

lst = [9,5,8,12]
#selection_sort_v1(lst)
bubble_sort(lst)
print lst

students = [['zhangsan',67], ['lisi',87],['wangwu',98]]
sum = 0
for student in students:
    sum += student[1]
avg = sum/float(len(students))
print avg
students.sort(key = lambda x : x[1], reverse = True)
print students


