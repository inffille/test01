from graphics import *

win = GraphWin("aaa", 600,300)

def draw_house(x, y, base_color="white", roof_color="red", has_roof_window=True):
	base = Rectangle(Point(x+100, y+100), Point(x+200,y+200))
	base.setFill(base_color)
	roof = Polygon(Point(x+98, y+100), Point(x+202, y+100), Point(x+150, y+50))
	roof.setFill(roof_color)
	roof_win = Circle(Point(x+150, y+75), 10)
	base.draw(win)
	roof.draw(win)
	if has_roof_window == True:
		roof_win.draw(win)

def draw_tree():
	pass

def draw_sun():
	pass

def draw_all():
	draw_house(0,0)
	draw_house(100,100, "black", "yellow", False)
	draw_tree()
	draw_sun()

draw_all()

win.getMouse()
win.close()
