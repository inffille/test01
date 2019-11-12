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
#		op1, op2, symbol = self.parse_input()
#		res = self.present_operation(op1, op2, symbol)
#		return res
		pass 
	
	def parse_input(self):
		pass

	def present_operation(self, op1, op2, symbol):
		n1 = number.Number(op1)
		n2 = number.Number(op2)
		op = operation.Operation(n1, n2, symbol)
		return op.result()

	def draw_result(self,res):
		pass		
