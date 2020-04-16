class detector():
	from Player import Player
	from Board import Board
	enemys = {'w':('d',0,'@'),'d':('w',1,'#')}
	check = [False,False]
	mate = [False,False]
	passant = [False,False]
	square = ()
	permition = [True,True]
	castles = [[True,True],[True,True]]

	def cheks(self):
		for i in range(8):
			for j in range(8):
				if self.Board.b1[i][j].__repr__()[0]=='K':
					if self.enemys[self.Board.b1[i][j].__repr__()[1]][0] in self.Board.b2[i][j]:
						detector.check[self.enemys[self.Board.b1[i][j].__repr__()[1]][1]] = True
					else:
						detector.check[self.enemys[self.Board.b1[i][j].__repr__()[1]][1]] = False

	def promotion(self):
		for i in range(0,8,7):
			for j in range(8):
				if self.Board.b1[i][j].__repr__()[0]=='P':
					color = self.Board.b1[i][j].__repr__()[1] 
					promotion = input('Choose a promotion , Ex: Q,R,B,N:\n')
					self.Player().spawn(promotion,color,i,j)
					self.Board().refresh()				

	def allplays(self,color1,passant):
		save1 = [[self.Board.b1[i][j] for j in range(8)]for i in range(8)]
		save2 = [[self.Board.b2[i][j]for j in range(8)]for i in range(8)]
		save3 = [detector.check[x] for x in range(2)]
		row = ('1','2','3','4','5','6','7','8')
		col = ('a','b','c','d','e','f','g','h')
		lista = []
		lista2 = []
		for i in range(8):
			for j in range(8):
				if self.Board.b1[i][j] != '  ':
					color2 = self.Board.b1[i][j].__repr__()[1]
					name = self.Board.b1[i][j].__repr__()[0]
					if color1 == color2:
						for x in range(8):
							for y in range(8):
								if name+color2+str(i)+str(j) in self.Board.b2[x][y] or name+self.enemys[color2][2]+str(i)+str(j) in self.Board.b2[x][y]:
									lista2.append(name+col[y]+row[x])						
		for x in range(len(lista2)):
			try:
				self.Player().play(lista2[x][0],color1,lista2[x][1],lista2[x][2],passant,detector.square)
				self.Board().refresh()
				self.cheks()
				if save1 == self.Board.b1 or detector.check[self.enemys[color1][1]] == True:
					pass
				else:	
					lista.append(lista2[x])
				self.Board.b1 = [[save1[i][j] for j in range(8)]for i in range(8)]
				self.Board.b2 = [[save2[i][j] for j in range(8)]for i in range(8)]
				detector.check = [save3[x] for x in range(2)]
			except:
				pass				
							
		if len(lista) == 0:
			print('check mate')
			detector.mate[self.enemys[color1][1]] = True
		else:
			detector.mate[self.enemys[color1][1]] = False	

	def passant_f(self,play,color,save1,board1):
		diferences = [] 
		if play[0]=='P':
			if play[4]=='4' and color=='w' or play[4]=='5' and color=='d':
				for i in range(8):
					for j in range(8):
						if save1[i][j]!=board1[i][j]:
							diferences.append((i,j))			
				if len(diferences)==2:
					squares = abs(diferences[0][0]-diferences[1][0])
					if squares == 2:
						detector.square = (min(diferences[0][0],diferences[1][0])+1,diferences[0][1])
						cols = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
						try:
							if 'P'+self.enemys[color][0] == board1[int(play[4])-1][cols[play[3]]+1].__repr__():
								detector.passant[0] = True
							elif 'P'+self.enemys[color][0] == board1[int(play[4])-1][cols[play[3]]-1].__repr__():
								detector.passant[1] = True
							else:
								detector.passant = [False,False]
						except:
							detector.passant = [False,False]
					else:
						detector.passant = [False,False]
			else:
				detector.passant = [False,False]
		else:
			detector.passant = [False,False]

	def castle(self,play,color,save1,board1):
		if detector.permition[self.enemys[color][1]] == True:
			if 'K' in play:
				detector.castles[self.enemys[color][1]][0] = False
				detector.castles[self.enemys[color][1]][1] = False
				detector.permition[self.enemys[color][1]] = False
			elif 'R' in play:
				rookmoviment = []
				for i in range(8):
					for j in range(8):
						if save1[i][j]!=board1[i][j]:
							rookmoviment.append(board1[i][j].__repr__()+str(i)+str(j))
				print(rookmoviment)			
				if len(rookmoviment)==2:
					print('ok')
					for x in rookmoviment:
						if '  ' in x:
							print('ok denovo')
							print(x[4]+x[5])
							if x[4]+x[5]=='00':
								detector.castles[0][0] = False
							elif x[4]+x[5]=='07':
								detector.castles[0][1] = False
							elif x[4]+x[5]=='77':
								detector.castles[1][1] = False
							elif x[4]+x[5]=='70':
								detector.castles[1][0] = False
									



										





		

