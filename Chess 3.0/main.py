from Board import Board
from Player import Player
from special_actions import detector
import os 


clear = lambda: os.system('cls')

def setposition(pos):
	if pos == 1:
		for x in range(8):
			Player().spawn('P','w',1,x)
			Player().spawn('P','d',6,x)
		Player().spawn('R','w',0,0)
		Player().spawn('R','w',0,7)
		Player().spawn('N','w',0,1)
		Player().spawn('N','w',0,6)
		Player().spawn('B','w',0,2)
		Player().spawn('B','w',0,5)
		Player().spawn('Q','w',0,3)
		Player().spawn('K','w',0,4)

		Player().spawn('R','d',7,0)
		Player().spawn('R','d',7,7)
		Player().spawn('N','d',7,1)
		Player().spawn('N','d',7,6)
		Player().spawn('B','d',7,2)
		Player().spawn('B','d',7,5)
		Player().spawn('Q','d',7,3)
		Player().spawn('K','d',7,4)

	if pos == 2:
		Player().spawn('K','d',4,0)
		Player().spawn('P','d',3,0)
		Player().spawn('P','w',2,0)
		Player().spawn('P','w',1,1)
		Player().spawn('R','w',5,7)

	if pos == 3:
		for x in range(8):
			Player().spawn('P','w',1,x)
			Player().spawn('P','d',6,x)
		Player().delete(1,4)
		Player().delete(6,4)	
		Player().spawn('R','w',0,0)
		Player().spawn('R','w',0,7)
		Player().spawn('Q','w',0,3)
		Player().spawn('K','w',0,4)
		Player().spawn('N','w',0,6)

		Player().spawn('R','d',7,0)
		Player().spawn('R','d',7,7)
		Player().spawn('Q','d',7,3)
		Player().spawn('K','d',7,4)
			
class main():
	def __init__(self):
		setposition(1)
		Board().refresh()
		turn = {0:'w',1:'d'}
		c=0
		'•'
		while True:
			color = turn[c%2] #change color
			#save the boards
			save1 = [[Board.b1[i][j] for j in range(8)]for i in range(8)]	
			save2 = [[Board.b2[i][j] for j in range(8)]for i in range(8)]

			#print the board
			prints = []
			print('\n\n\n')
			for x in range(7,-1,-1):
				for z in range(8):
					if Board.b1[x][z]=='  ':
						prints.append(' *')
					else:
						prints.append(Board.b1[x][z])	

				print('     ',x+1,'',prints[0],prints[1],prints[2],prints[3],prints[4],prints[5],prints[6],prints[7])
				prints=[]
			print('')
			print('        ','a ','b ','c ','d ','e ','f ','g ','h \n\n\n')				
			play = input('make a move for %s:\n'%color)
			if play=='stop':
				break	
			try:	
				Player().play(play[0],play[1],play[2],play[3],color)
			except:
				pass
	
			Board().refresh()
			detector().checks()
			clear()
			if True in detector.check:
				print('       \\\\---------check---------//')

			#if the player make a move in check
			error = False
			if color == 'd' and detector.check[1]== True or color == 'w' and detector.check[0]== True:
				error = True

			if Board.b1==save1 or error==True:
				Board.b1 = [[save1[i][j] for j in range(8)]for i in range(8)]	
				Board.b2 = [[save2[i][j] for j in range(8)]for i in range(8)]
				print('      \\\\---------Error---------//')
				c-=1
			else:	
				detector().passant_f(play,save1,Board.b1)
				detector().promotion()

			if True in detector.check:
				detector().allplays(turn[(c+1)%2])
			c+=1
main()



