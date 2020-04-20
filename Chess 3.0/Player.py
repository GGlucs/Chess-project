class Player():
	from Pieces import Pieces
	from Board import Board
	#conversion cordinates of chess to python int
	cols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
	rows = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}

	def spawn(self,name,color,row,col):
		self.Board.b1[row][col] = self.Pieces(name,color,row,col)

	def delete(self,row,col):
		self.Board.b1[row][col] = '  '

	def move(self,name,color,row1,col1,row2,col2):	
		self.Board.b1[row1][col1].stop= False
		self.Board.b1[row2][col2] = self.Board.b1[row1][col1]
		self.delete(row1,col1)

	def play(self,col1,row1,col2,row2,turn):
		c1 = self.cols[col1]
		c2 = self.cols[col2]
		r1 = self.rows[row1]
		r2 = self.rows[row2]
		enemy = self.Board.b1[r1][c1].enemy
		name = self.Board.b1[r1][c1].__repr__()[0]
		color = self.Board.b1[r1][c1].__repr__()[1]
		square = self.Board.b1[r2][c2]

		if name+color != '  ' and color==turn:
			if name=='P':

				#normal move to pawns
				if name+self.Board.b1[r1][c1].pmark+str(r1)+str(c1) in self.Board.b2[r2][c2] and square=='  ':
					self.move(name,color,r1,c1,r2,c2)

				#attack pawn
				elif name+color+str(r1)+str(c1) in self.Board.b2[r2][c2] and square.__repr__()[1]== enemy:
					self.move(name,color,r1,c1,r2,c2)

				#passant
				elif name+color+str(r1)+str(c1) in self.Board.b2[r2][c2]: 	
					if self.Board.b1[r1][c1].passant[1]== True and c2 == c1-1:
						self.move(name,color,r1,c1,r2,c2)
						self.delete(r1,c1-1)

					elif self.Board.b1[r1][c1].passant[0]== True and c2 == c1+1:
						self.move(name,color,r1,c1,r2,c2)
						self.delete(r1,c1+1)

			#another pieces		
			elif name+color+str(r1)+str(c1) in self.Board.b2[r2][c2]:
				if square == '  ' or square.__repr__()[1]!= color:
					self.move(name,color,r1,c1,r2,c2)

			#castle
			elif name=='K':
				if name+self.Board.b1[r1][c1].pmark+str(r1)+str(c1) in self.Board.b2[r2][c2]:
					sqking = ''.join(self.Board.b2[r1][4:7])
					kg1 = self.Board.b1[r1][c1+2]
					kg2 = self.Board.b1[r1][c1+1] 
					sqqueen = ''.join(self.Board.b2[r1][2:5])
					qg1 = self.Board.b1[r1][c1-1]
					qg2 = self.Board.b1[r1][c1-2]
					qg3 = self.Board.b1[r1][c1-3]

					if c2 == 6 and enemy not in sqking and kg1=='  ' and kg2=='  ':
						self.move(name,color,r1,c1,r2,c2)
						self.move('R',color,r1,7,r2,5)
					elif c2 == 2 and enemy not in sqqueen and qg1=='  ' and qg2=='  ' and qg3 == '  ':
						self.move(name,color,r1,c1,r2,c2)
						self.move('R',color,r1,0,r2,3)





	
