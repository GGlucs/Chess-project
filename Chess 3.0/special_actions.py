class detector():
	from Player import Player
	from Board import Board
	cols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
	rows = {'1':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7}
	colornum = {'w':0,'d':1}
	check = [False,False]
	mate = [False,False]

	#detect a check in the board
	def checks(self):
		for i in range(8):
			for j in range(8):
				if self.Board.b1[i][j].__repr__()[0]=='K':
					if self.Board.b1[i][j].enemy in self.Board.b2[i][j]:
						detector.check[self.Board.b1[i][j].num] = True
					else:
						detector.check[self.Board.b1[i][j].num] = False

	#promotion of pawns					
	def promotion(self):
		for i in range(0,8,7):
			for j in range(8):
				if self.Board.b1[i][j].__repr__()[0]=='P':
					color = self.Board.b1[i][j].__repr__()[1] 
					promotion = input('Choose a promotion , Ex: Q,R,B,N:\n')
					self.Player().spawn(promotion,color,i,j)
					self.Board().refresh()
					self.checks()

	#all possible plays,will search all pieces of the color
	#search all attacks of that pieces and add to a list1
	#and it will test all plays in the list1 and will add to
	#to another list2, if list2==0 >>> checkmate=True
	def allplays(self,color1):
		save1 = [[self.Board.b1[i][j] for j in range(8)]for i in range(8)]
		save2 = [[self.Board.b2[i][j]for j in range(8)]for i in range(8)]
		save3 = [detector.check[x] for x in range(2)]
		row = ('1','2','3','4','5','6','7','8')
		col = ('a','b','c','d','e','f','g','h')
		lista = []
		lista2 = []
		for i in range(8):
			for j in range(8):
				if self.Board.b1[i][j] != '':
					color2 = self.Board.b1[i][j].__repr__()[1]
					name = self.Board.b1[i][j].__repr__()[0]
					if color1 == color2:
						for x in range(8):
							for y in range(8):
								if name+color2+str(i)+str(j) in self.Board.b2[x][y] or name+self.Board.b1[i][j].pmark+str(i)+str(j) in self.Board.b2[x][y]:
									lista2.append(col[j]+row[i]+col[y]+row[x])						
		for x in lista2:
			try:
				self.Player().play(x[0],x[1],x[2],x[3],color1)
				self.Board().refresh()
				self.checks()
				if save1 == self.Board.b1 or detector.check[self.colornum[color1]] == True:
					pass
				else:	
					lista.append(x)
				self.Board.b1 = [[save1[i][j] for j in range(8)]for i in range(8)]
				self.Board.b2 = [[save2[i][j] for j in range(8)]for i in range(8)]
				detector.check = [save3[x] for x in range(2)]
			except:
				pass				

		if len(lista) == 0:
			print('     \\\\-------check mate-------//')
			detector.mate[self.colornum[color1]] = True
		else:
			detector.mate[self.colornum[color1]] = False	

	#detect passant and reset everytime
	def passant_f(self,play,save1,Board1):
		for i in range(8):
			for j in range(8):
				if Board1[i][j].__repr__()[0]=='P':
					if True in Board1[i][j].passant:
						Board1[i][j].passant[0]=False
						Board1[i][j].passant[1]=False
						break

		if 'P' == save1[self.rows[play[1]]][self.cols[play[0]]].__repr__()[0]:
			enemy = save1[self.rows[play[1]]][self.cols[play[0]]].enemy
			if abs(int(play[3])-int(play[1]))==2:
				if self.cols[play[2]]-1>= 0:
					sqleft = Board1[self.rows[play[3]]][self.cols[play[2]]-1].__repr__()
					if sqleft == 'P'+enemy:
						Board1[self.rows[play[3]]][self.cols[play[2]]-1].passant[0]=True

				if self.cols[play[2]]+1<= 7:
					sqright = Board1[self.rows[play[3]]][self.cols[play[2]]+1].__repr__()
					if sqright == 'P'+enemy:
						Board1[self.rows[play[3]]][self.cols[play[2]]+1].passant[1]=True




										





		

