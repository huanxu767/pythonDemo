#coding=UTF-8
# function
def add(x,y):
    z = x + y
    return z

res = add(3,5)
print res

# if
a = 30
b = 20
if a>b:
    print 'a bigger'
elif a == b:
    print 'equal'
else:
    print('a smaller')

# while
print "while"
v = 1
# v = raw_input("Enter a number")
# print "you entered:",v
while v < 10:
    print v
    v = v + 1



# for
for i in 'python':
    print i

fruits = ['apple','banana','mango']
for fruit in fruits:
    print fruit
    # if fruit == 'banana':
    #     break
else:
    print 'ok'

# list
demoList = [1,2,3,4]
print demoList[0]
print demoList[2]
demoList[0] = 10
print demoList
del demoList[0]
print demoList
demoList.append(20)
print demoList
demoList.append("hello")
print demoList
demoList += [100,200]
print demoList
demoList = demoList * 2
print demoList
print len(demoList)
print 20 in demoList
print demoList.count(20)
print demoList.index(20)

#元祖tuple
aTuple = ('e',23,123,88.8)
print aTuple

# Dictionary
dict = {'username':'xuhuan','password':'1234'}
print dict['username']
print dict.keys()
for key in dict:
    print dict[key]

dict['username'] = 123
print dict
del dict["password"]
print dict
