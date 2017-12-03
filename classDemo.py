class Employee:
    classSpec = "this a test class"
    __primaryname = "si you de "
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def hello(self):
        # print 'asdasdads'
        print "hello,"+self.name + ",your salary is " + str(self.salary)


worker = Employee("xiaoxu",100000)
worker.hello()
print worker.salary