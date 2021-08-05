class Employee:
	def __init__(self,first=None,last=None,pay=None):
		self.first=first
		self.last=last
		self.pay=pay
	def fulname(self):
		print(self.first+self.last)
	def raise_salary(self):
		raise_amount=1.04
		self.salary=int(self.pay*raise_amount)
		print(self.salary)
class Manager(Employee):
	def data(self):
		self.first=input("Enter first name: ")
		self.last=input("Enter last name: ")
		self.pay=int(input("Enter the pay: "))
	def raise_salary(self):
		raise_amount=1.10
		self.salary=int(self.pay*raise_amount)
		print(self.salary)
class Developer(Employee):
	def data(self):
		self.first=input("Enter first name: ")
		self.last=input("Enter last name: ")
		self.pay=int(input("Enter the pay: "))
	def raise_salary(self):
		raise_amount=1.08
		self.salary=int(self.pay*raise_amount)
		print(self.salary)
obj=Employee()
obj1=Manager()
obj1.data()
obj2=Developer()
obj2.data()
while True:
	print("1=> Full Name of Manager")
	print("2=> Full Name of Developer")
	print("3=> Salary of Manager")
	print("4=> Salary of Developer")
	print("5=> Exit")
	ch=int(input("Enter the choice: "))
	if ch == 1:
		print("Manager Name: ",obj1.fulname())
	if ch ==2:
		print("Developer Namee: ",obj2.fulname())
	if ch == 3:
		print("Manager salary: ",obj1.raise_salary())
	if ch == 4:
		print("Developer salary: ",obj2.raise_salary())
	if ch == 5:
		break

