import number
import operation
import tkinter as tk

class Display:
	def __init__(self):
		self.root = tk.Tk()
		self.lbl = tk.Label(self.root, text = "Insert Numbers")
		self.lbl.grid(row = 0, column = 0)
		self.entry = tk.Entry(self.root)
		self.entry.grid(row = 0, column = 1)

		self.root.mainloop()

	def process_input(self):
		string = self.entry.get()	
		op1,  symbol, op2 = self.parse_input(string)
		res = self.present_operation(op1, op2, symbol)
		return res
		  
	
	def parse_input(self, string):
		if len(string.split()) == 3:
			return string.split()
		else:
			raise Exception('You entered wrong number of parameters')

	def present_operation(self, op1, op2, symbol):
		n1 = number.Number(op1)
		n2 = number.Number(op2)
		op = operation.Operation(n1, n2, symbol)
		return op.result()

	def draw_result(self,res):
		pass		
