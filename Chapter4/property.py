class Employee:
	firstname:str = ''
	lastname:str = ''

	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	@property
	def fullname(self):
		return f'{self.firstname} {self.lastname}'

	@fullname.setter
	def fullname(self, name):
		self.firstname, self.lastname = name.split(' ')

	@fullname.deleter
	def fullname(self):
		self.firstname = None
		self.lastname = None

	'''
	def getFullname(self):
		return f'{self.firstname} {self.lastname}'

	def setFullname(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def deleter(self):
		self.firstname = None
		self.lastname = None

e1 = Employee('Dre', 'dogu')

print(e1.getFullname())
e1.setFullname('AA', 'dogu')
print(e1.getFullname())
e1.deleter()
print(e1.getFullname())
'''

e1 = Employee('Dre', 'dogu')

print(e1.fullname)
e1.fullname = 'AA dre'
print(e1.fullname)
del e1.fullname
print(e1.fullname)

a = 3.1415752

print(f"${a:,.2f}")
