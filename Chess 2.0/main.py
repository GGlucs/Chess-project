from Player import Player
from Board import Board
from special_actions import detector
from pygame_functions import *
import os
'''
screen = screenSize(504,600)
pygame.display.set_caption('Chess 2.0')	

instructionLabel = makeLabel('make a move:',60,0,510,'red','Agency FB')
showLabel(instructionLabel)

board = pygame.image.load('board.png')
dking = pygame.image.load('dking.png')
dqueen = pygame.image.load('dqueen.png')
dbishop = pygame.image.load('dbishop.png')
dknight = pygame.image.load('dknight.png')
drook = pygame.image.load('drook.png')
dpawn = pygame.image.load('dpawn.png')
wking = pygame.image.load('wking.png')
wqueen = pygame.image.load('wqueen.png')
wbishop = pygame.image.load('wbishop.png')
wknight = pygame.image.load('wknight.png')
wrook = pygame.image.load('wrook.png')
wpawn = pygame.image.load('wpawn.png')

board = pygame.transform.scale(board,(504,504))
dking = pygame.transform.scale(dking,(58,60))
wking = pygame.transform.scale(wking,(55,58))
dqueen = pygame.transform.scale(dqueen,(60,60))
wqueen = pygame.transform.scale(wqueen,(55,60))
dbishop = pygame.transform.scale(dbishop,(57,60))
wbishop = pygame.transform.scale(wbishop,(57,60))
dknight = pygame.transform.scale(dknight,(60,60))
wknight = pygame.transform.scale(wknight,(60,60))
drook = pygame.transform.scale(drook,(60,61))
wrook = pygame.transform.scale(wrook,(60,61))
dpawn = pygame.transform.scale(dpawn,(53,50))
wpawn = pygame.transform.scale(wpawn,(60,50))


pies = {'Pw':wpawn,'Qw':wqueen,'Nw':wknight,'Rw':wrook,'Kw':wking,'Bw':wbishop,'Pd':dpawn,'Qd':dqueen,'Nd':dknight,'Rd':drook,'Kd':dking,'Bd':dbishop}
'''
clear = lambda: os.system('cls')

color = {0:'w',1:'d'}
enemy = {0:'d',1:'w'}

class Main():
	list_plays = []
	def __init__(self):
		for x in range(8):
			Player().spawn('P','d',6,x)
			Player().spawn('P','w',1,x)

		Player().spawn('K','d',7,4)
		Player().spawn('Q','d',7,3)
		Player().spawn('R','d',7,0)
		Player().spawn('R','d',7,7)
		Player().spawn('N','d',7,1)
		Player().spawn('N','d',7,6)
		Player().spawn('B','d',7,2)
		Player().spawn('B','d',7,5)

		Player().spawn('K','w',0,4)
		Player().spawn('Q','w',0,3)
		Player().spawn('R','w',0,0)
		Player().spawn('R','w',0,7)
		Player().spawn('N','w',0,1)
		Player().spawn('N','w',0,6)
		Player().spawn('B','w',0,2)
		Player().spawn('B','w',0,5)

		Board().refresh()
		c = 0
		check = False

		while True:
			save1 = [[Board.b1[i][j] for j in range(8)]for i in range(8)]
			save2 = [[Board.b2[i][j] for j in range(8)]for i in range(8)]
			save_passant = [detector.passant[x] for x in range(2)]

			#screen.blit(board,(0,0))
			#for i in range(8):
			#	for j in range(8):
			#		if Board.b1[i][j] != '  ':
			#			nam = Board.b1[i][j].__repr__()
			#			if nam == 'Pw' or nam == 'Pd':
			#				ac = 14
			#			else:
			#				ac = 5
			#			screen.blit(pies[nam],(63*j,441-(63*i)+ac))	


			#wordBox = makeTextBox(5,550,300,0,'HERE',0,24)
			#showTextBox(wordBox)
			#jogada = textBoxInput(wordBox)
			for x in range(7,-1,-1):
				print(Board.b1[x])
			jogada = input('digite uma jogada:\n')	
			if jogada == 'stop':
				break	
			jogada = Player().translate(jogada)
			print(jogada)
			try:
				Player().play3(jogada,color[c%2],detector.passant,detector.square,detector.castles)
			except:
				pass				
			detector().promotion()
			detector().passant_f(jogada,color[c%2],save1,Board.b1)
			Board().refresh()
			detector().cheks()
			detector().castle(jogada,color[c%2],save1,Board.b1)
			clear()

			if True in detector.check:
				print('check')
				detector().allplays(enemy[c%2],detector.passant)

			self.erro = False
			if color[c%2] == 'd' and detector.check[1] == True or color[c%2] == 'w' and detector.check[0] == True:
				print(color[c%2],detector.check[1])
				self.erro = True

			if save1 == Board.b1 or self.erro == True:
				Board.b1 = [[save1[i][j] for j in range(8)]for i in range(8)]
				Board.b2 = [[save2[i][j] for j in range(8)]for i in range(8)]
				detector.passant = save_passant
				detector().cheks()
				print('\\\\---------ERROR---------//')
				continue

			Main.list_plays.append(jogada[0]+color[c%2]+jogada[-2]+jogada[-1])
			c+=1
		#endWait()		
Main()

