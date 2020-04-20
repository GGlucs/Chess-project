class Board():
	from sympy import cos,pi
	#board b1 for pieces and b2 for attacks
	b1 = [['  'for i in range(8)]for x in range(8)]
	b2 = [[''for i in range(8)]for x in range(8)]


	def refresh(self):
		#reset b2
		Board.b2 = [[''for i in range(8)]for x in range(8)]

		for i in range(8):
			for j in range(8):
				if self.b1[i][j] != '  ':

					#knight movement
					if self.b1[i][j].__repr__()[0] == 'N':
						for x in range(0,4): 
							row = abs(2*self.cos(x*self.pi/3)-self.cos(x*self.pi))
							col = 2*self.cos(x*self.pi/3)
							if i+row <= 7 and 0<=j+col<=7:
								self.b2[i+row][j+col]+=str(self.b1[i][j])+str(i)+str(j)
							if i-row >= 0 and 0<=j+col<=7:
								self.b2[i-row][j+col]+=str(self.b1[i][j])+str(i)+str(j)
						continue 
						
					#this loops will make the attacks of all pieces	
					for x in range(1,self.b1[i][j].attacks[0]):#Left
						if j-x>=0:
							self.b2[i][j-x]+=str(self.b1[i][j])+str(i)+str(j)
							if self.b1[i][j-x] != '  ':
								break

					for x in range(1,self.b1[i][j].attacks[1]):#Right
						if j+x<=7:
							self.b2[i][j+x]+=str(self.b1[i][j])+str(i)+str(j)
							if self.b1[i][j+x] != '  ':
								break

					for x in range(1,self.b1[i][j].attacks[2]):#up
						if i+x<=7:
							self.b2[i+x][j]+=str(self.b1[i][j])+str(i)+str(j)
							if self.b1[i+x][j] != '  ':
								break

					for x in range(1,self.b1[i][j].attacks[3]):#down
						if i-x>=0:
							self.b2[i-x][j]+=str(self.b1[i][j])+str(i)+str(j)
							if self.b1[i-x][j] != '  ':
								break

					for x in range(1,self.b1[i][j].attacks[4]):#left down
						if i-x>=0 and j-x>=0:
							self.b2[i-x][j-x]+=str(self.b1[i][j])+str(i)+str(j)
							if self.b1[i-x][j-x] != '  ':
								break

					for x in range(1,self.b1[i][j].attacks[5]):#right down
						if i-x>=0 and j+x<=7:
							self.b2[i-x][j+x]+=str(self.b1[i][j])+str(i)+str(j)
							if self.b1[i-x][j+x] != '  ':
								break

					for x in range(1,self.b1[i][j].attacks[6]):#right up
						if i+x<=7 and j+x<=7:
							self.b2[i+x][j+x]+=str(self.b1[i][j])+str(i)+str(j)
							if self.b1[i+x][j+x] != '  ':
								break

					for x in range(1,self.b1[i][j].attacks[7]):#left up
						if i+x<=7 and j-x>=0:
							self.b2[i+x][j-x]+=str(self.b1[i][j])+str(i)+str(j)
							if self.b1[i+x][j-x] != '  ':
								break

					#a diferent symbol for pawns, they doesn't do a front attack
					if self.b1[i][j].__repr__()[0] == 'P':
						if self.b1[i][j].__repr__()[1] == 'w':
							if i == 1:
								for x in range(1,3):
									self.b2[i+x][j]+= 'P@'+str(i)+str(j)
									if self.b1[i+x][j] != '  ':
										break
							elif i != 7:
								self.b2[i+1][j]+='P@'+str(i)+str(j)

						elif self.b1[i][j].__repr__()[1] == 'd':
							if i == 6:
								for x in range(1,3):
									self.b2[i-x][j]+= 'P#'+str(i)+str(j)
									if self.b1[i-x][j] != '  ':
										break
							elif i != 0:
								self.b2[i-1][j]+='P#'+str(i)+str(j)

					#a diferent for castle for king, if the king moved, it will not happens
					if self.b1[i][j].__repr__() == 'Kw':
						if i == 0 and j == 4:
							if self.b1[i][j+3].__repr__()=='Rw':
								if self.b1[i][j].stop== True and self.b1[i][j+3].stop== True:
									self.b2[i][j+2]+= 'K@'+str(i)+str(j)
							if self.b1[i][j-4].__repr__()=='Rw':		
								if self.b1[i][j].stop== True and self.b1[i][j-4].stop== True:
									self.b2[i][j-2]+= 'K@'+str(i)+str(j)

					if self.b1[i][j].__repr__() == 'Kd':
						if i == 7 and j == 4:
							if self.b1[i][j+3].__repr__()=='Rd':
								if self.b1[i][j].stop== True and self.b1[i][j+3].stop== True:
									self.b2[i][j+2]+= 'K#'+str(i)+str(j)
							if self.b1[i][j-4].__repr__()=='Rd':		
								if self.b1[i][j].stop== True and self.b1[i][j-4].stop== True:
									self.b2[i][j-2]+= 'K#'+str(i)+str(j)			

									