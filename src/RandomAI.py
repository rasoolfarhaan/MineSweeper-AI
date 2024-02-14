import random
from AI import AI
from Action import Action


class RandomAI ( AI ):
	
	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):
		self.__rowDimension = rowDimension
		self.__colDimension = colDimension
		self.__moveCount = 0


	def getAction(self, number: int) -> "Action Object":
		while self.__moveCount < 5:
			action = AI.Action(random.randrange(1, len(AI.Action)))
			x = random.randrange(self.__colDimension)
			y = random.randrange(self.__rowDimension)
			self.__moveCount += 1
			return Action(action, x, y)

		action = AI.Action(random.randrange(len(AI.Action)))
		x = random.randrange(self.__colDimension)
		y = random.randrange(self.__rowDimension)

		return Action(action, x, y)