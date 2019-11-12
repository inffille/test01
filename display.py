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

	def run(self):
		self.root.bind('<Button-1>', self.process_input)
		self.root.mainloop()

	def process_input(self, event):
		string = self.entry.get()	
		op1,  symbol, op2 = self.parse_input(string)
		res = self.present_operation(op1, op2, symbol)
		self.draw_result(res)
		  
	
	def parse_input(self, string):
		if len(string.split()) == 3:
			return string.split()
		else:
			raise Exception('You entered wrong number of parameters')

	def present_operation(self, op1, op2, symbol):
		n1 = number.Number(int(op1))
		n2 = number.Number(int(op2))
		if symbol == '+':
			op = operation.Plus(n1, n2)
		return op.result()

	def draw_result(self,res):
		print(str(res))
