import pygame
import random
# from src import hero
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2
    '''
   Creates rectangle objects for the x and y coordinates of the enemy. Also sets up the speed and name of the enemy.
    Args:
      self[str]: instance variable
      name[str]: name of the enemy object
      x[int]: x location of enemy object
      y[int]: y location of the enemy object
      img_file[str]: calls an image that the enemy uses as the sprite
    Return: 
      None
    '''

    def update(self):
      movement = [-1, 0, 1]
      self.rect.x += random.choice(movement)
      self.rect.y += random.choice(movement)
      if int(self.rect.x) > 640:
        self.rect.x = 0
      elif self.rect.x < 0:
        self.rect.x = 640
      elif self.rect.y < 0:
        self.rect.y = 480
      elif self.rect.y > 480:
        self.rect.y = 0
      print(self.rect.x)
      print(self.rect.y)
    '''
   Moves the enemy object by a random value from -1 to 1. Also moves the enemy object to the opposite side of the screen if the enemy leaves the bounds.
    Args:
      self[str]: instance variable
    Return: 
      None
    '''
      
      
      # print("'Update me,' says " + self.name)
