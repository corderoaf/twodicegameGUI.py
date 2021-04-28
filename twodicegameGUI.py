"""
Program: twodicegameGUI.py (Final Project)
Author: Angel_Cordero 04.28.2021
"""

from breezypythongui import EasyFrame
import random


class TwoDiceGame(EasyFrame):

	def __init__(self):
		
		EasyFrame.__init__(self, title = "Two Dice Game", resizable = False, background = "black")
		
		self.addLabel(text = "Human Vs. Computer Dice Game", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "black", foreground = "lightseagreen").config(font = ("Helvetica", 20))

		self.addLabel(text = "*** Die One for Human ***", row = 1, column = 0, sticky = "NSEW", background = "grey", foreground = "orange", font = 20)
		self.rollOne = self.addIntegerField(value = 0, row = 2, column = 0, rowspan = 2, sticky = "NW")
		self.rollOne["background"] = "olivedrab"
		self.rollOne["foreground"] = "orange"
		self.rollOne["font"] = 21

		self.addLabel(text = "*** Die Two for Computer ***", row = 1, column = 1, sticky = "NSEW", background ="grey", foreground = "orange", font = 20)
		self.rollTwo = self.addIntegerField(value = 0, row = 2, column = 1, rowspan = 2)
		self.rollTwo["background"] = "olivedrab"
		self.rollTwo["foreground"] = "orange"
		self.rollTwo["font"] = 21

		self.button = self.addButton(text = "Ready, Said, Roll", row = 4 , column = 0, columnspan = 2, command = self.roll)
		self.button["background"] = "orange"
		self.button["foreground"] = "olivedrab"
		self.button["font"] = 20

		self.resultArea = self.addLabel(text = "", row = 5 , column = 0, columnspan = 2, rowspan = 3, sticky = "NSEW")
		self.resultArea["background"] = "black"
		self.resultArea["foreground"] = "lightseagreen"	
		self.resultArea["font"] = 60	

	def roll(self):
		roll1 = random.randint(1, 6)
		roll2 = random.randint(1, 6)
		result = ""

		if roll1 > roll2:
			result = "The Human Is The Winner!"
		elif roll1 < roll2:
			result = "The Computer Is Ths Winner!"
		else:
			 roll1 == roll2
			 result = "It's a tie! Try again!!"

		self.rollOne.setNumber(roll1)
		self.rollTwo.setNumber(roll2)
		self.resultArea["text"] = result

def main():
		TwoDiceGame().mainloop()
main()