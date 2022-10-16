class test():
	def __init__(self,name):
		self.name=name
	def getname(self):
		return self.name
	def setname(self,name):
		self.name = name
	na = property(getname,setname)

te=test('掌扇三')
print(te.na)
print(1)
		
