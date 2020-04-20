class Pieces():
	#info contains ,0 the enemy,1 another symbol to color,2 a number identity
	info = {'w':('d','@',0),'d':('w','#',1)}

	#castle left and right for black and white
	castle = [[True,True],[True,True]]

	def __init__(self,name,color,row,col):

		self.color = color
		self.name = name
		self.row = row
		self.col = col
		self.enemy = self.info[color][0]
		self.num = self.info[color][2]
		self.pmark = self.info[color][1]
		self.stop = True #self.stop will detect a move

		#pieces will receive 8 numbers that represents
		#the attack in the directions ,up, down,left... 
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
			self.passant = [False,False]#left,right
			if self.color == 'w':
				self.attacks = (0,0,0,0,0,0,2,2)

			elif self.color == 'd':
				self.attacks = (0,0,0,0,2,2,0,0)

	def __repr__(self):
		return self.name+self.color			

		

