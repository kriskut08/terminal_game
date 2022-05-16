from pynput import keyboard
import os as os
import json


#board = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
#        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
#        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
#        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
#        ['-', '-', '#', '-', '-', '-', '-', '-', '-', '-'], 
#        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
#        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
#        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
#        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], 
#        ['-', '-', '-', '-', '-', '-', '-', '-', '-', '#']]


#open tabla.json and load it's content into a variable
f = open("tabla.json")
l = json.load(f)

board = []

for i in l['tabla']:
	s = i.split(' ')
	board.append(s)



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
        # Stop listener
		return False


x,y = int(l["kezdes"][0]),int(l["kezdes"][2])

def move(key):
	global x,y
	if key == keyboard.Key.left or key == 'a':
		if y>0 and board[x][y-1] != '#':
			board[x][y]= '-'
			y-=1
			board[x][y] = 'X'
	if key == keyboard.Key.right or key == 'd':
		if y<9 and board[x][y+1] != '#':
			board[x][y]= '-'
			y+=1
			board[x][y] = 'X'
	if key == keyboard.Key.up or key == 'w':
		if x>0 and board[x-1][y] != '#':
			board[x][y]= '-'
			x-=1
			board[x][y] = 'X'
	if key == keyboard.Key.down or key == 's':
		if x<9 and board[x+1][y] != '#':
			board[x][y]= '-'
			x+=1
			board[x][y] = 'X'
	
#a játék kezdete:
clear() 
print(l["message"])
board[x][y] = 'X'
printboard(board)

with keyboard.Listener(on_release=on_release) as listener:
    listener.join()