#ndn is a python based dice roller

#
# usage: python ndn.py amount size modifier
#
# e.g. python ndn.py 1 20 0
# This would roll 1 d20 with no modifier

import sys
import random

class Roll:
	def __init__(self,amount,size,modifier):
		self.amount = amount
		self.size = size
		self.modifier = modifier

	def roll(self):
		values = []
		for i in range(0,self.amount):
			randvalue = random.randint(1,self.size)
			values.append(randvalue)
		return sum(values) + self.modifier

if __name__ == "__main__":
	roll1d20 = Roll(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
	print roll1d20.roll()
