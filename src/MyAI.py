from enum import Enum, unique
from AI import AI
from Action import Action

@unique
class PieceType(Enum):
	BOMB = 0
	UNCOVERED = 1
	COVERED = 2

class Tile():

	def __init__(self, r, c, pc, number=0, effective=0, uNeighbors=8):
		self.r = r
		self.c = c
		self.pieceType = pc
		self.number = number
		self.effective = effective
		self.uNeighbors = uNeighbors

class MyAI( AI ):

	def __init__(self, rowDimension, colDimension, totalMines, startX, startY):

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		self.rows = rowDimension
		self.cols = colDimension
		self.totalMines = totalMines
		self.minesLeft = totalMines
		self.prevX = startX
		self.prevY = startY
		self.uncovers = rowDimension * colDimension - totalMines - 1
		self.board = [[Tile(r, c, PieceType.COVERED) for c in range(colDimension)] for r in range(rowDimension)]
		for c in range(self.cols):
			if c == 0 or c == self.cols - 1:
				self.board[0][c].uNeighbors = 3
				self.board[self.rows - 1][c].uNeighbors = 3
			else:
				self.board[0][c].uNeighbors = 5
				self.board[self.rows - 1][c].uNeighbors = 5
		for r in range(self.rows):
			if r == 0 or r == self.rows - 1:
				self.board[r][0].uNeighbors = 3
				self.board[r][self.cols - 1].uNeighbors = 3
			else:
				self.board[r][0].uNeighbors = 5
				self.board[r][self.cols - 1].uNeighbors = 5
		# self.printBoardEffective()
		# self.printNeighbors()

		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################
	
	def updateNeighbors(self, tile):
		left = tile.c - 1
		right = tile.c + 1
		up = tile.r - 1
		down = tile.r + 1
		if (left >= 0):
			self.board[tile.r][left].uNeighbors-=1
		if (right < self.cols):
			self.board[tile.r][right].uNeighbors -=1
		if (up >= 0):
			self.board[up][tile.c].uNeighbors -=1
		if (down < self.rows):
			self.board[down][tile.c].uNeighbors -=1
		if (left >= 0 and up >= 0):
			self.board[up][left].uNeighbors -=1
		if (left >= 0 and down < self.rows):
			self.board[down][left].uNeighbors -=1
		if (right < self.cols and up >= 0):
			self.board[up][right].uNeighbors -=1
		if (right < self.cols and down < self.rows):
			self.board[down][right].uNeighbors -=1

	def updateEffective(self, tile: Tile):
		left = tile.c - 1
		right = tile.c + 1
		up = tile.r - 1
		down = tile.r + 1
		if (left >= 0):
			if (self.board[tile.r][left].pieceType == PieceType.BOMB):
				tile.effective -= 1
		if (right < self.cols):
			if (self.board[tile.r][right].pieceType == PieceType.BOMB):
				tile.effective -= 1
		if (up >= 0):
			if (self.board[up][tile.c].pieceType == PieceType.BOMB):
				tile.effective -= 1
		if (down < self.rows):
			if (self.board[down][tile.c].pieceType == PieceType.BOMB):
				tile.effective -= 1
		if (left >= 0 and up >= 0):
			if (self.board[up][left].pieceType == PieceType.BOMB):
				tile.effective -= 1
		if (left >= 0 and down < self.rows):
			if (self.board[down][left].pieceType == PieceType.BOMB):
				tile.effective -= 1
		if (right < self.cols and up >= 0):
			if (self.board[up][right].pieceType == PieceType.BOMB):
				tile.effective -= 1
		if (right < self.cols and down < self.rows):
			if (self.board[down][right].pieceType == PieceType.BOMB):
				tile.effective -= 1

	
				
	def flagBombs(self, tile: Tile):
		left = tile.c - 1
		right = tile.c + 1
		up = tile.r - 1
		down = tile.r + 1
		if (left >= 0):
			if (self.board[tile.r][left].pieceType == PieceType.COVERED):
				self.markBomb(self.board[tile.r][left])
		if (right < self.cols):
			if (self.board[tile.r][right].pieceType == PieceType.COVERED):
				self.markBomb(self.board[tile.r][right])
		if (up >= 0):
			if (self.board[up][tile.c].pieceType == PieceType.COVERED):
				self.markBomb(self.board[up][tile.c])
		if (down < self.rows):
			if (self.board[down][tile.c].pieceType == PieceType.COVERED):
				self.markBomb(self.board[down][tile.c])
		if (left >= 0 and up >= 0):
			if (self.board[up][left].pieceType == PieceType.COVERED):
				self.markBomb(self.board[up][left])
		if (left >= 0 and down < self.rows):
			if (self.board[down][left].pieceType == PieceType.COVERED):
				self.markBomb(self.board[down][left])
		if (right < self.cols and up >= 0):
			if (self.board[up][right].pieceType == PieceType.COVERED):
				self.markBomb(self.board[up][right])
		if (right < self.cols and down < self.rows):
			if (self.board[down][right].pieceType == PieceType.COVERED):
				self.markBomb(self.board[down][right])

	def markBomb(self, tile: Tile):
		tile.pieceType = PieceType.BOMB
		left = tile.c - 1
		right = tile.c + 1
		up = tile.r - 1
		down = tile.r + 1
		if (left >= 0):
			if (self.board[tile.r][left].pieceType == PieceType.UNCOVERED):
				self.board[tile.r][left].effective -= 1
			self.board[tile.r][left].uNeighbors -= 1
		if (right < self.cols):
			if (self.board[tile.r][right].pieceType == PieceType.UNCOVERED):
				self.board[tile.r][right].effective -= 1
			self.board[tile.r][right].uNeighbors -= 1	
		if (up >= 0):
			if (self.board[up][tile.c].pieceType == PieceType.UNCOVERED):
				self.board[up][tile.c].effective -= 1
			self.board[up][tile.c].uNeighbors -= 1	
		if (down < self.rows):
			if (self.board[down][tile.c].pieceType == PieceType.UNCOVERED):
				self.board[down][tile.c].effective -= 1
			self.board[down][tile.c].uNeighbors -= 1
		if (left >= 0 and up >= 0):
			if (self.board[up][left].pieceType == PieceType.UNCOVERED):
				self.board[up][left].effective -= 1
			self.board[up][left].uNeighbors -= 1
		if (left >= 0 and down < self.rows):
			if (self.board[down][left].pieceType == PieceType.UNCOVERED):
				self.board[down][left].effective -= 1
			self.board[down][left].uNeighbors -= 1
		if (right < self.cols and up >= 0):
			if (self.board[up][right].pieceType == PieceType.UNCOVERED):
				self.board[up][right].effective -= 1
			self.board[up][right].uNeighbors -= 1
		if (right < self.cols and down < self.rows):
			if (self.board[down][right].pieceType == PieceType.UNCOVERED):
				self.board[down][right].effective -= 1
			self.board[down][right].uNeighbors -= 1

	def findUnmarkedNeighbor(self, tile: Tile):
		left = tile.c - 1
		right = tile.c + 1
		up = tile.r - 1
		down = tile.r + 1
		if (left >= 0):
			if (self.board[tile.r][left].pieceType == PieceType.COVERED):
				self.prevX = left
				self.prevY = tile.r
				return Action(AI.Action.UNCOVER, left, tile.r)
		if (right < self.cols):
			if (self.board[tile.r][right].pieceType == PieceType.COVERED):
				self.prevX = right
				self.prevY = tile.r
				return Action(AI.Action.UNCOVER, right, tile.r)
		if (up >= 0):
			if (self.board[up][tile.c].pieceType == PieceType.COVERED):
				self.prevX = tile.c
				self.prevY = up
				return Action(AI.Action.UNCOVER, tile.c, up)
		if (down < self.rows):
			if (self.board[down][tile.c].pieceType == PieceType.COVERED):
				self.prevX = tile.c
				self.prevY = down
				return Action(AI.Action.UNCOVER, tile.c, down)
		if (left >= 0 and up >= 0):
			if (self.board[up][left].pieceType == PieceType.COVERED):
				self.prevX = left
				self.prevY = up
				return Action(AI.Action.UNCOVER, left, up)
		if (left >= 0 and down < self.rows):
			if (self.board[down][left].pieceType == PieceType.COVERED):
				self.prevX = left
				self.prevY = down
				return Action(AI.Action.UNCOVER, left, down)
		if (right < self.cols and up >= 0):
			if (self.board[up][right].pieceType == PieceType.COVERED):
				self.prevX = right
				self.prevY = up
				return Action(AI.Action.UNCOVER, right, up)
		if (right < self.cols and down < self.rows):
			if (self.board[down][right].pieceType == PieceType.COVERED):
				self.prevX = right
				self.prevY = down
				return Action(AI.Action.UNCOVER, right, down)
		
	def getAction(self, number: int) -> "Action Object":

		########################################################################
		#							YOUR CODE BEGINS						   #
		########################################################################
		# update the board
		lastPiece = self.board[self.prevY][self.prevX]
		lastPiece.pieceType = PieceType.UNCOVERED
		lastPiece.number = number
		lastPiece.effective = number

		# update new piece's effective number and neighbors
		self.updateNeighbors(lastPiece)
		self.updateEffective(lastPiece)

		# print("NUMBER IS: " + str(self.uncovers))
		# print()
		# self.printBoardEffective()
		# print()
		# self.printNeighbors()
		if self.uncovers == 0:
			return Action(AI.Action.LEAVE)

		for r in range(self.rows):
			for c in range(self.cols):
				tile = self.board[r][c]
				if(tile.pieceType == PieceType.UNCOVERED and tile.effective == tile.uNeighbors):
					self.flagBombs(tile)

		for r in range(self.rows):
			for c in range(self.cols):
				tile = self.board[r][c]
				if(tile.pieceType == PieceType.UNCOVERED and tile.effective == 0 and tile.uNeighbors > 0):
					self.uncovers -= 1
					return self.findUnmarkedNeighbor(tile)
		for r in range(self.rows):
			for c in range(self.cols):
				tile = self.board[r][c]
				if(tile.pieceType == PieceType.COVERED):
					self.uncovers -= 1
					self.prevX = c
					self.prevY = r
					return Action(AI.Action.UNCOVER, c, r)
		########################################################################
		#							YOUR CODE ENDS							   #
		########################################################################

	def printBoardNormal(self):
		for r in range(len(self.board)):
			for c in range(len(self.board[0])):
				if self.board[r][c].pieceType == PieceType.COVERED:
					print("- ", end="")
				elif self.board[r][c].pieceType == PieceType.BOMB:
					print("B ", end="")
				elif self.board[r][c].pieceType == PieceType.UNCOVERED:
					print(str(self.board[r][c].number) + ' ', end="")
			print()

	def printNeighbors(self):
		for r in range(len(self.board)):
			for c in range(len(self.board[0])):
				print(str(self.board[r][c].uNeighbors) + ' ', end="")
			print()

	def printBoardEffective(self):
		for r in range(len(self.board)):
			for c in range(len(self.board[0])):
				if self.board[r][c].pieceType == PieceType.COVERED:
					print("- ", end="")
				elif self.board[r][c].pieceType == PieceType.BOMB:
					print("B ", end="")
				elif self.board[r][c].pieceType == PieceType.UNCOVERED:
					print(str(self.board[r][c].effective) + ' ', end="")
			print()