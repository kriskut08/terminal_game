from pynput import keyboard
import os as os
import json

f = open("tabla.json")
l = json.load(f)




def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


def printboard(game):
	print("╭──────────────────────────────╮")
	for i in range(len(game)):
		print("│ ",end='')
		for j in range(len(game[i])):
			if j<9:
				print(game[i][j],end = "  ")
			else:
				print(game[i][j],end=' │')
		print("",end='\n')
	print("╰──────────────────────────────╯")


def on_release(key):
	clear()
	move(key)
	printboard(board)
	if key == keyboard.Key.esc:
		return False

jelek = ["#","C"]
tabla = -1
x,y = int(l["kezdes"][0]),int(l["kezdes"][2])

def load_board():
	global board
	global tabla
	global l
	global x
	global y
	x,y = int(l["kezdes"][0]),int(l["kezdes"][2])
	tabla += 1
	print(tabla)
	board = []
	try:
		for i in l['tabla{0}'.format(str(tabla))]:
			s = i.split(' ')
			board.append(s)
	except:
		print(l["exit_message"])
		quit()		
	board[x][y] = 'X'


def move(key):
	global x,y
	if key == keyboard.Key.left or key == 'a':
		if y>0 and board[x][y-1] not in jelek:
			board[x][y]= '-'
			y-=1
			board[x][y] = 'X'
		else:
			if board[x][y-1] == 'C':
				load_board()
	if key == keyboard.Key.right or key == 'd':
		if y<9 and board[x][y+1] not in jelek:
			board[x][y]= '-'
			y+=1
			board[x][y] = 'X'
		else:
			if board[x][y+1] == 'C':
				load_board()
	if key == keyboard.Key.up or key == 'w':
		if x>0 and board[x-1][y] not in jelek:
			board[x][y]= '-'
			x-=1
			board[x][y] = 'X'
		else:
			if board[x-1][y] == 'C':
				load_board()
	if key == keyboard.Key.down or key == 's':
		if x<9 and board[x+1][y] not in jelek:
			board[x][y]= '-'
			x+=1
			board[x][y] = 'X'
		else:
			if board[x+1][y] == 'C':
				load_board()
	
#a játék kezdete:
def start():
	load_board()
	clear() 
	print(l["message"])
	board[x][y] = 'X'
	printboard(board)

	with keyboard.Listener(on_release=on_release) as listener:
		listener.join()
if tabla==-1:
    start()