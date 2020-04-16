class Player():
	from Pieces import Pieces
	from Board import Board
	cols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
	rows = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
	enemys = {'w':('d','@',0,0,1),'d':('w','#',7,1,+1)}

	def spawn(self,name,color,row,col):
		self.Board.b1[row][col] = self.Pieces(name,color)

	def delete(self,row,col):
		self.Board.b1[row][col] = '  '

	def move(self,name,color,col,row,mark):	
		self.spawn(name,color,row,col)
		pos = self.Board.b2[row][col].index(name+mark)
		r = int(self.Board.b2[row][col][pos+2])
		c = int(self.Board.b2[row][col][pos+3])
		self.delete(r,c)
		
	def play(self,name,color,col,row,passant,square):
		self.row = self.rows[row]
		self.col = self.cols[col]
		if name == 'P':
			
			if self.enemys[color][1] in self.Board.b2[self.row][self.col] and self.Board.b1[self.row][self.col] == '  ':
				self.move(name,color,self.col,self.row,self.enemys[color][1])

			elif True in passant or self.Board.b1[self.row][self.col].__repr__()[1] == self.enemys[color][0] and 'P'+color in self.Board.b2[self.row][self.col]:
				self.move(name,color,self.col,self.row,color)
				if passant[0] == True and square==(self.row,self.col):
					self.delete(self.row+self.enemys[color][4],self.col)
				elif passant[1] == True and square==(self.row,self.col):
					self.delete(self.row+self.enemys[color][4],self.col)

		elif name+color in self.Board.b2[self.row][self.col] and name != 'P':
			if self.Board.b1[self.row][self.col] == '  ' or color != self.Board.b1[self.row][self.col].__repr__()[1]:
				self.move(name,color,self.col,self.row,color)

	def play2(self,vetor,color,passant,square):
		pawn = False
		if vetor[0]=='P':
			if 'P'+color in self.Board.b2[self.rows[vetor[4]]][self.cols[vetor[3]]]:
				self.spawn('P',color,self.rows[vetor[4]],self.cols[vetor[3]])
				pos = self.Board.b2[self.rows[vetor[4]]][self.cols[vetor[3]]].index('P'+color)
				r = int(self.Board.b2[self.rows[vetor[4]]][self.cols[vetor[3]]][pos+2])
				c = self.cols[vetor[1]]
				self.delete(r,c)
				if passant[0] == True and square==(self.rows[vetor[4]],self.cols[vetor[3]]):
					self.delete(r,c-1)
				elif passant[1] == True and square==(self.rows[vetor[4]],self.cols[vetor[3]]):
					self.delete(r,c+1)	

		elif self.Board.b2[self.rows[vetor[4]]][self.cols[vetor[3]]].count(vetor[0]+color) == 2:
			try:
				for x in range(8):
					if vetor[0]+color == self.Board.b1[x][self.cols[vetor[1]]].__repr__():
						self.spawn(vetor[0],color,self.rows[vetor[4]],self.cols[vetor[3]])
						self.Board.b1[x][self.cols[vetor[1]]] = '  '
						break
			except:
				for x in range(8):
					if vetor[0]+color in self.Board.b1[self.rows[vetor[1]]][x].__repr__():
						self.spawn(vetor[0],color,self.rows[vetor[4]],self.cols[vetor[3]])
						self.Board.b1[self.rows[vetor[1]]][x] = '  '
						break

	def play3(self,vetor,color,passant,square,castles):
		if vetor == '0-0' or vetor == '0-0-0':
			self.play_castle(vetor,color,castles)
		elif vetor[2] == 'x':
			if self.Board.b1[self.rows[vetor[-1]]][self.cols[vetor[-2]]]!='  ' or True in passant:
				if vetor[1] == '0':
					self.play(vetor[0],color,vetor[-2],vetor[-1],passant,square)
				else:	
					self.play2(vetor,color,passant,square)
		elif vetor[2] != 'x':
			if self.Board.b1[self.rows[vetor[-1]]][self.cols[vetor[-2]]]=='  ':
				if vetor[1] == '0':
					self.play(vetor[0],color,vetor[-2],vetor[-1],passant,square)
				else:	
					self.play2(vetor,color,passant,square)

	def play_castle(self,vetor,color,castles):
		if vetor =='0-0':
			if castles[self.enemys[color][3]][1] == True:
				if self.Board.b1[self.enemys[color][2]][6]=='  ' and self.Board.b1[self.enemys[color][2]][5]=='  ':
					if self.enemys[color][0] not in self.Board.b2[self.enemys[color][2]][6]:
						if self.enemys[color][0] not in self.Board.b2[self.enemys[color][2]][5]:
							if self.enemys[color][0] not in self.Board.b2[self.enemys[color][2]][4]:
								self.spawn('K',color,self.enemys[color][2],6)
								self.spawn('R',color,self.enemys[color][2],5)
								self.delete(self.enemys[color][2],4)
								self.delete(self.enemys[color][2],7)

		if vetor =='0-0-0':
			if castles[self.enemys[color][3]][0] == True:
				if self.Board.b1[self.enemys[color][2]][1]=='  ' and self.Board.b1[self.enemys[color][2]][2]=='  ' and self.Board.b1[self.enemys[color][2]][3]=='  ':
					if self.enemys[color][0] not in self.Board.b2[self.enemys[color][2]][2]:
						if self.enemys[color][0] not in self.Board.b2[self.enemys[color][2]][3]:
							if self.enemys[color][0] not in self.Board.b2[self.enemys[color][2]][4]:
								self.spawn('K',color,self.enemys[color][2],2)
								self.spawn('R',color,self.enemys[color][2],3)
								self.delete(self.enemys[color][2],4)
								self.delete(self.enemys[color][2],0)

	def translate(self,s):
		lista = ['K','Q','R','N','B']
		if s[0] not in lista:
			s = 'P'+s 
		string = s[0]+'00'+s[1:]
		vetor = [string[0],string[-4],string[-3],string[-2],string[-1]]
		if vetor[2] !='x':
			vetor[1] = vetor[2]
			vetor[2] = '0'
		if s == 'P0-0' or s == 'P0-0-0':
			vetor = s[1:]
		return vetor						


