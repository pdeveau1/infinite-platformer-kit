import pygame, random

class Platforms(pygame.sprite.Sprite):
  def __init__(self,pos,img_path,width = 70,height = 70):
    super().__init__()
    self.image = pygame.Surface([width,height]).convert()
    self.image.blit(pygame.image.load(img_path).convert(),(0,0),(0,0,width,height))
    self.image.set_colorkey((0,0,0))
    self.rect = self.image.get_rect()
    self.rect.center = pos

  def scroll(self, change):
    #create a variable for display Info
    #screen_info = pygame.display.Info()
    self.rect.top += change
    #create an if statement that checks if the platform has reached the bottom of the screen and if it has reset it to the top of the screen
    #if self.rect.top > screen_info.current_h:
      #self.rect.top = -50
      #self.rect.left = random.randint(5,(screen_info.current_w)//10)*10