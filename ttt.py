import random
import os

a1=0
a2=0
a3=0
b1=0
b2=0
b3=0
c1=0
c2=0
c3=0

def print_box():
	print "*********************"
	print "*      *      *     *"
	print "*   %d  *   %d  *  %d  *" %(a1,a2,a3)
	print "*      *      *     *"
	print "*********************"
	print "*      *      *     *"
	print "*   %d  *   %d  *  %d  *" %(b1,b2,b3)
	print "*      *      *     *"
	print "*********************"
	print "*      *      *     *"
	print "*   %d  *   %d  *  %d  *" %(c1,c2,c3)
	print "*      *      *     *"
	print "*********************"

def system_play():
	global a1,a2,a3,b1,b2,b3,c1,c2,c3
	x = random.randint(1,9)
	if x == 1:
		if a1 == 1 or a1 == 2:
			system_play()
		else:
			a1 = 2
	if x == 2:
		if a2 == 1 or a2 == 2:
			system_play()
		else:
			a2 = 2
	if x == 3:
		if a3 == 1 or a3 == 2:
			system_play()
		else:
			a3 = 2
	if x == 4:
		if b1 == 1 or b1 == 2:
			system_play()
		else:
			b1 = 2
	if x == 5:
		if b2 == 1 or b2 == 2:
			system_play()
		else:
			b2 = 2
	if x == 6:
		if b3 == 1 or b3 == 2:
			system_play()
		else:
			b3 = 2
	if x == 7:
		if c1 == 1 or c1 == 2:
			system_play()
		else:
			c1 = 2
	if x == 8:
		if c2 == 1 or c2 == 2:
			system_play()
		else:
			c2 = 2
	if x == 9:
		if c3 == 1 or c3 == 2:
			system_play()
		else:
			c3 = 2
	print_box()
	system_check()

def system_check():
	global a1,a2,a3,b1,b2,b3,c1,c2,c3
	if a1 == 2:
		if a1 == a2 and a2 == a3:
			print "System Won"
			os._exit(1)
		if a1 == b1 and b1 == c1:
			print "System Won"
			os._exit(1)
		if a1 == b2 and b2 == c3:
			print "System Won"
			os._exit(1)
	if a2 == 2:
		if a2 == b2 and b2 == c2:
			print "System Won"
			os._exit(1)
	if a3 == 2:
		if a3 == b3 and b3 == c3:
			print "System Won"
			os._exit(1)
		if a3 == b2 and b2 == c1:
			print "System Won"
			os._exit(1)
	if b1 == 2:
		if b1 == b2 and b2 == b3:
			print "System Won"
			os._exit(1)
	if c1 == 2:
		if c1 == c2 and c2 == c3:
			print "System Won"
			os._exit(1)
	draw_check()
	player_play()


def player_check():
	global a1,a2,a3,b1,b2,b3,c1,c2,c3
	if a1 == 1:
		if a1 == a2 and a2 == a3:
			print "You Won"
			os._exit(1)
		if a1 == b1 and b1 == c1:
			print "You Won"
			os._exit(1)
		if a1 == b2 and b2 == c3:
			print "You Won"
			os._exit(1)
	if a2 == 1:
		if a2 == b2 and b2 == c2:
			print "You Won"
			os._exit(1)
	if a3 == 1:
		if a3 == b3 and b3 == c3:
			print "You Won"
			os._exit(1)
		if a3 == b2 and b2 == c1:
			print "You Won"
			os._exit(1)
	if b1 == 1:
		if b1 == b2 and b2 == b3:
			print "You Won"
			os._exit(1)
	if c1 == 1:
		if c1 == c2 and c2 == c3:
			print "You Won"
			os._exit(1)
	draw_check()
	system_play()


def player_play():
	print "Enter 2 digit box number:"
	global a1,a2,a3,b1,b2,b3,c1,c2,c3
	x = int(raw_input())
	if x == 11:
		if a1 == 1 or a1 == 2:
			print "Play again"
			player_play()
		else:
			a1 = 1
	elif x == 12:
		if a2 == 1 or a2 == 2:
			print "Play again"
			player_play()
		else:
			a2 = 1
	elif x == 13:
		if a3 == 1 or a3 == 2:
			print "Play again"
			player_play()
		else:
			a3 = 1
	elif x == 21:
		if b1 == 1 or b1 == 2:
			print "Play again"
			player_play()
		else:
			b1 = 1
	elif x == 22:
		if b2 == 1 or b2 == 2:
			print "Play again"
			player_play()
		else:
			b2 = 1
	elif x == 23:
		if b3 == 1 or b3 == 2:
			print "Play again"
			player_play()
		else:
			b3 = 1
	elif x == 31:
		if c1 == 1 or c1 == 2:
			print "Play again"
			player_play()
		else:
			c1 = 1
	elif x == 32:
		if c2 == 1 or c2 == 2:
			print "Play again"
			player_play()
		else:		
			c2 = 1
	elif x == 33:
		if c3 == 1 or c3 == 2:
			print "Play again"
			player_play()
		else:	
			c3 = 1
	else:
		print "veredi enter chesnav ra howle"
		player_play()
	print_box()
	player_check()

def draw_check():
	global a1,a2,a3,b1,b2,b3,c1,c2,c3
	if (a1 == 1 or a1 == 2) and (a2 == 1 or a2 == 2) and (a3 == 1 or a3 == 2) and (b3 == 1 or b3 == 2) and (b2 == 1 or b2 == 2) and (b1 == 1 or b1 == 2) and (c3 == 1 or c3 == 2) and (c2 == 1 or c2 == 2) and (c1 == 1 or c1 == 2):
		print "Game drawn :)"
		os._exit(1)

print_box()
player_play()