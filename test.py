#!/usr/bin/python
import pygame
pygame.init()

class Hangman():
  def __init__(self):
    self.lines = 0 #Number of lines to be drawn

  def hang(self):
    self.lines += 1

  def draw(self,screen):
    for x in range(self.lines):
      coord1 = (x*10,20)
      coord2 = (x*10,50)
      pygame.draw.line(screen,(0,0,0),coord1,coord2)

size = screenWidth,screenHeight = 200,70
screen = pygame.display.set_mode(size)
pygame.display.flip()

myman = Hangman()

drawlist = []
drawlist.append(myman)
#mainloop
running = True
while running:
  #EVENT HANDLING#
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == 32: #Spacebar
        myman.hang()

  #DRAWING#
  screen.fill((255,255,255))
  for item in drawlist:
    item.draw(screen)
  pygame.display.flip()
