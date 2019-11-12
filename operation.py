import number

class Operation:
	def __init__(self,symbol_of_operation,operand1,operand2):
		self.type = symbol_of_operation
		self.entries = [operand1,operand2]
	
	"""
	Return value of Number, type int or float.
	"""
	def result(self):
		pass
	
	def get_op(self):
		return str(self.entries[0])+self.type+str(self.entries[1])

class Plus(Operation):
	def __init__(self,operand1,operand2):
		super().__init__('+',operand1,operand2)
	
	def result(self):
		return self.entries[0].value+self.entries[1].value
	
	def print_result(self):
		return self.get_op() + '=' + str(self.result())


