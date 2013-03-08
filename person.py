class Person:	

    def __init__(self):
	self.__name = 'chen'
	self.__id = '0807505207'

    def say_id(self):
	print "%s's id is %s" %(self.__name,self.__id)

    def set_name(self,name):
	self.__name = name

    def set_id(self,id):
	self.__id = id

me = Person()
me.set_id('08007505207')
me.set_name('HuiXiao')
me.say_id()

