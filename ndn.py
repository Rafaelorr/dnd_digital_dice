#ndn is a python based dice roller

#
# usage: python ndn.py amount size modifier
#
# e.g. python ndn.py 1 20 0
# This would roll 1 d20 with no modifier

import sys
import random

class Roll:
	def __init__(self,amount,size,modifier,advantage):
		self.amount:int = amount
		self.size:int = size
		self.modifier:int = modifier
		self.advantage:str = advantage

	def roll(self) -> int:
		values :list[int] = []
		if self.advantage == "a":
			for _ in range(self.amount):
				roll1 = random.randint(0,self.size)
				roll2 = random.randint(0,self.size)
				values.append(max(roll1,roll2))
		elif self.advantage == "d":
			for _ in range(self.amount):
				roll1 = random.randint(0,self.size)
				roll2 = random.randint(0,self.size)
				values.append(min(roll1,roll2))
		else:
			for _ in range(self.amount):
				randvalue:int = random.randint(1,self.size)
				values.append(randvalue)
		return sum(values) + self.modifier

if __name__ == "__main__":
	roll1d20 = Roll(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]), str(sys.argv[4]))
	print(roll1d20.roll())
