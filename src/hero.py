import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
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
        self.name = name
        self.speed = 3
        self.health = 3
    '''
   Creates rectangle objects for the x and y coordinates of the hero. Also creates the speed, health, and name of the hero.
    Args:
      self[str]: instance variable
      name[str]: name of the hero object
      x[int]: x location of hero object
      y[int]: y location of the hero object
      img_file[str]: calls an image that the hero uses as the sprite
    Return: 
      None
    '''
    #methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= self.speed
    '''
   Moves the hero object up when called upon.
    Args:
      self[str]: instance variable
    Return: 
      None
    '''
    def move_down(self):
        self.rect.y += self.speed
    '''
   Moves the hero object down when called upon.
    Args:
      self[str]: instance variable
    Return: 
      None
    '''
    
    def move_left(self):
        self.rect.x -= self.speed
    '''
   Moves the hero object left when called upon.
    Args:
      self[str]: instance variable
    Return: 
      None
    '''
    def move_right(self):
        self.rect.x += self.speed
    '''
   Moves the hero object right when called upon.
    Args:
      self[str]: instance variable
    Return: 
      None
    '''
    
    def update(self):
      if int(self.rect.x) > 640:
          self.rect.x = 0
      elif self.rect.x < 0:
        self.rect.x = 640
      elif self.rect.y < 0:
        self.rect.y = 480
      elif self.rect.y > 480:
        self.rect.y = 0
    '''
   Moves the hero object to the opposite side of the screen if the hero leaves the bounds.
    Args:
      self[str]: instance variable
    Return: 
      None
    '''

    def fight(self, opponent):
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True
    '''
   Moves the hero object down when called upon.
    Args:
      self[str]: instance variable
    Return: 
     [bool]: returns False if the hero collides with an enemy and the health decreases by one.
    [bool]: returns True if the hero collides with an enemy and the health doesn't decrease by one.
    '''
