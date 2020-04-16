class Pieces():
	def __init__(self,name,color):

		self.color = color
		self.name = name
		self.attacks = ()

		if self.name == 'Q':
			self.attacks = (8,8,8,8,8,8,8,8)

		if self.name == 'R':
			self.attacks = (8,8,8,8,0,0,0,0)
		
		if self.name == 'B':
			self.attacks = (0,0,0,0,8,8,8,8)

		if self.name == 'K':
			self.attacks = (2,2,2,2,2,2,2,2)

		if self.name == 'N':
			self.attacks = (2,2,2,2,2,2,2,2)	

		if self.name == 'P':
			if self.color == 'w':
				self.attacks = (0,0,0,0,0,0,2,2)

			elif self.color == 'd':
				self.attacks = (0,0,0,0,2,2,0,0)

	def __repr__(self):
		return self.name+self.color			

		
