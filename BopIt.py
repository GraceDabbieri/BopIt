import sys
import os
import pygame
import random
import wx
def dialog(title, text):
	app = wx.App(False)
	frame = wx.Frame(None, wx.ID_ANY, title)
	dialog = wx.MessageDialog(frame, text, title, wx.OK)
	dialog.ShowModal()
	dialog.Destroy()
	frame.Destroy()
	app.MainLoop()
def score(points):
	points = ("Your score is: " + str(points))
	dialog("Score", points)
def fail():
	files = [file for file in os.listdir("gameSounds/fail") if os.path.isfile(os.path.join("gameSounds/fail", file))]
	failure = random.choice(files)
	pygame.mixer.Sound(os.path.join("gameSounds", "screem.ogg")).play()
	pygame.time.delay(1000)
	pygame.mixer.Sound(os.path.join("gameSounds", "jingle.ogg")).play()
	pygame.time.delay(1500)  
	pygame.mixer.Sound(os.path.join("gameSounds/fail", failure)).play()
	pygame.time.delay(1000) 
def command():
	move = random.choice(["b", "t", "p", "f", "s"])
	x = pygame.mixer.Sound(os.path.join("gameSounds", move + ".ogg")) 
	x.play()
	pygame.time.delay(400)  # Wait for 0.4 seconds
	x = pygame.mixer.Sound(os.path.join("gameSounds", "1.ogg"))
	x.play()
	pygame.time.delay(200) 
	x = pygame.mixer.Sound(os.path.join("gameSounds", "2.ogg"))
	x.play()
	pygame.time.delay(200)
	start_time = pygame.time.get_ticks()
	response_time = 3000
	while True:
		event = pygame.event.poll()
		if event.type == pygame.KEYDOWN:
			if event.key == getattr(pygame, f"K_{move}"):
				y = pygame.mixer.Sound(os.path.join("gameSounds", move + "-end.ogg"))
				y.play()
				pygame.time.delay(300)
				y = pygame.mixer.Sound(os.path.join("gameSounds", "1.ogg"))
				y.play()
				pygame.time.delay(200)
				y = pygame.mixer.Sound(os.path.join("gameSounds", "3.ogg"))
				y.play()
				pygame.time.delay(120)
				y.play()
				pygame.time.delay(200)
				return True
			else:
				return False
		if pygame.time.get_ticks() - start_time > response_time:
			return False
def main():
	pygame.init()
	pygame.mixer.init()
	WINDOW_WIDTH = 640
	WINDOW_HEIGHT = 480
	window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	pygame.display.set_caption("Bop It!")
	count = 0
	start = pygame.mixer.Sound(os.path.join("gameSounds", "start.ogg"))
	start.play()
	pygame.time.delay(1800)
	running = True
	while running:
		success = command()
		if success:
			count += 1
		else:
			fail()
			pygame.time.delay(900)
			score(count)
			running = False
	pygame.quit()
if __name__ == "__main__":
	intro = ("This is a computer version of the game Bop It.\nTo play, perform the command the computer shouts out by pressing the correct key on your keyboard. The game will start when you press okay on this dialog.\nBop it: the letter b\nTwist it: the letter t\nPull it: the letter p\nFlick it: the letter f\nSpinn it: the letter s.\nEnjoy.")
	dialog("Welcome to bop it!", intro)
	main()
#This program was written by Grace Dabbieri