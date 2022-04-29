class Person :
	# id = 0
	def __init__(self, name , age) :
		self.name = name
		self.age = age
		self.identity = id
		id += 1

	def print_info(self) :
		print("person name is :",self.name)
		print("person age is :", self.age)
		print("person id is :", self.identity)

	p1 = Person("Mustafa",25)
	p2 = Person("Salma", 21)
	p3 = Person("Elham", 54)

	p1.print_info()