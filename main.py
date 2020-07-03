import sys, pygame, random
from pygame.locals import*
from platformers import*
from player import*

pygame.init()
screen_info = pygame.display.Info()

#set the width and height to the size of the screen
size = (width,height) = (int(screen_info.current_w),int(screen_info.current_h))
screen = pygame.display.set_mode(size)

#create clock object
clock = pygame.time.Clock()
#create color RGB
color = (255,224,179)
#fill screen with color
screen.fill(color)
#create Sprite groups
sprite_list = pygame.sprite.Group()
platforms = pygame.sprite.Group()
player = ''

def get_player_actions():
  #creating dictionary of player images
  p1_actions = {}
  #adding jump image to dictionary
  p1_actions["p1_jump"] = pygame.image.load("images/p1_jump.png").convert()
  #set transparent background
  p1_actions["p1_jump"].set_colorkey((0,0,0))
  #adding hurt image to dictionary
  p1_actions["p1_hurt"] = pygame.image.load("images/p1_hurt.png").convert()
  #set background to transparent
  p1_actions["p1_hurt"].set_colorkey((0,0,0))
  return p1_actions

def init(p1_actions):
  global player
  for i in range(height//100):
    for j in range(width//420):
      plat = Platforms((random.randint(5, (width-50) // 10)*10,120*i),'images/grassHalf.png',70,40)
      platforms.add(plat)
  #create player in the center and above the last platform
  player = Player((platforms.sprites()[-1].rect.centerx,platforms.sprites()[-1].rect.centery-300),p1_actions)
  #add player to sprite group
  sprite_list.add(player)
font = pygame.font.SysFont(None,70)
#create main function
def main():
  global player
  game_over = False
  p1_actions = get_player_actions()
  init(p1_actions)
  while True:
    #set maximum refresh rate
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      #check if any key is pressed
      if event.type == KEYDOWN:
        #check if it is f key
        if event.key == K_f:
          #make screen full screen
          pygame.display.set_mode(size, FULLSCREEN)
        #check if escape key pressed
        if event.key == K_ESCAPE:
          #reset to original size
          pygame.display.set_mode(size)
        if event.key == K_r and game_over:
          player.kill()
          init(p1_actions)
          game_over = False
    keys = pygame.key.get_pressed()
    #check if left keys is being pressed
    if keys[pygame.K_LEFT]:
      player.left()
    #check if right key is being pressed
    if keys[pygame.K_RIGHT]:
      player.right()
    if player.update(platforms):
      game_over = True
    #set screen color
    screen.fill(color)
    #add images to screen
    text = font.render("Score: {}".format(player.progress),True,(255,0,0))
    text_rect = text.get_rect()
    platforms.draw(screen)
    sprite_list.draw(screen)
    screen.blit(text,text_rect)
    pygame.display.flip()


if __name__ == "__main__":
  main()