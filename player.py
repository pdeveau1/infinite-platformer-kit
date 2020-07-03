import pygame

class Player(pygame.sprite.Sprite):
  def __init__(self,pos,images):
    super().__init__()
    self.images = images
    self.image = images['p1_jump']
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.xy_speed = pygame.math.Vector2(0, 0)
    self.facing = "R"
    self.jump_speed = -14
    self.world_y = 0
    self.progress = 0

  def update(self,platforms):
    screen_info = pygame.display.Info()
    #check if player is near end of screen
    if self.rect.top >= screen_info.current_h - 80:
      #switch image to look like falling
      self.image = self.images["p1_hurt"]
    else:
      #otherwise keeps it as jumping image
      self.image = self.images["p1_jump"]
    #update the image and direction
    if self.facing == "L":
      #flip on x-axis
      self.image = pygame.transform.flip(self.image,True,False)
    #move the player
    self.rect.move_ip(self.xy_speed)
    self.xy_speed[0] = 0

    #check if hitting wall and moving to other side
    if self.rect.right < 0:
      self.rect.left = screen_info.current_w
    elif self.rect.left > screen_info.current_h:
      self.rect.right = 0
    self.world_y += self.xy_speed[1]*-1
    if self.world_y > self.progress:
      self.progress = self.world_y
    #scroll platforms down
    if self.rect.top < 100:
      self.rect.top = 100
      for plat in platforms.sprites():
        plat.scroll(-1*self.xy_speed[1])
    #check if fallen off world
    elif self.rect.top > screen_info.current_h -80:
      self.rect.top = screen_info.current_h - 80
      for plat in platforms.sprites():
        if plat.rect.bottom > 0:
          plat.scroll(-1*self.xy_speed[1])
        else:
          plat.kill()
      return True
    #check if player hit amy platforms
    hit_list = pygame.sprite.spritecollide(self, platforms,False)

    for plat in hit_list:
      #player landed on top of platform
      if self.xy_speed[1] > 0 and abs(self.rect.bottom - plat.rect.top) <= self.xy_speed[1]:
        self.rect.bottom = plat.rect.top
        self.xy_speed[1] = self.jump_speed

    #create gravity
    self.xy_speed[1] += .5

  def left(self):
    #set facing variable to L(left)
    self.facing == "L"
    #move character to left
    self.xy_speed[0] = -6

  def right(self):
    #set facing variable to R(right)
    self.facing == "R"
    #move character to right
    self.xy_speed[0] = 6
      