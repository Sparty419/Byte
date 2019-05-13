class a:
	def __init__(self,b):
		self.b = b

	def getstring(self):
		self.b = input("enter value: ")
		

	def printstring(self):
		return self.b.upper()


test = a("")

test.getstring()
print(test.printstring())


