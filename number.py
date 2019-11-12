class Number:
	def __init__(self, value, sign):
		self.value = value
		self.sign = sign
		self.type = type(self.value)
		if self.type not in (int, float):
			self.type = 'other'
			raise TypeError('Not a number!')
	
	def getNumber(self):
		return self.value
