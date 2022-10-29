class Employee:
	firstName:str = ''
	lastName:str = ''
	price:float = ''
	idNumber:str = ''

	def __init__(self, firstName, lastName, price, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.price = price
		self.idNumber = idNumber

	@property
	def fullname(self):
		return f'{self.firstName} {self.lastName}'

	@fullname.setter
	def fullname(self, name):
		self.firstName, self.lastName = name.split(' ')

	@fullname.deleter
	def fullname(self):
		self.firstName = None
		self.lastName = None

	@property
	def prices(self):
		return self.price

	@prices.setter
	def prices(self, price):
		self.price = price

	@prices.deleter
	def prices(self):
		self.price = 0

	@property
	def idNo(self):
		return self.idNumber

	@idNo.setter
	def idNo(self, idNumber):
		self.idNumber = idNumber

	@idNo.deleter
	def idNo(self):
		self.idNumber = None

	def print(self):
		print(f'{self.fullname} ${self.price:.2f} {self.idNumber}')

e1 = Employee('Dre', 'GO', 5000, 'abcd123')
e1.fullname = 'Dre dogu'
e1.idNo = '444555'
e1.print()