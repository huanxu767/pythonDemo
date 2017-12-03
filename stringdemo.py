var1 = "hello world"
var2 = '''das'k'l""jdsal'''

print var1
print var2

print var1[0]
print var1[-1]
print var1[0:5]
print var1[2:5]
print var1[:5]
print var1 in 'hell'
print var1 not in 'hell'

print 'hello\n'
print r'hello\n'

print "my name is %s and age is %d " % ('Mike', 18)


var1 = "abcdefgcdcd"
print var1.find('cd')
print var1.find('cd',5)
print var1.find('cd',2)
print var1.count('cd')
print var1.find('cd',2,len(var1))

print "-"*10
print var1.index('cd')
print var1.replace("cd","wo")
print var1.replace("cd","wo",1)

print var1.split("b")
print var1.split("cd")
print var1.split("cd",2)

# print var1.decode(encoding='UTF-8')












