import pygame
import player

pygame.init()

WIDTH = 1280
HEIGHT = 720
FPS = 60

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")

player = player.Player(100,200)

def main():
  run = True
  
  right = False
  left = False
  up = False
  down = False
  fire = False
  
  while run:
    clock.tick(FPS)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False 
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          run = False
        if event.key == pygame.K_d:
          right = True
        if event.key == pygame.K_a:
          left = True
        if event.key == pygame.K_w:
          up = True
        if event.key == pygame.K_s:
          down = True
        
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
          right = False
        if event.key == pygame.K_a:
          left = False 
        if event.key == pygame.K_w:
          up = False
        if event.key == pygame.K_s:
          down = False
      
    player.draw(screen)
    player.move(right, left, up, down) 
    player.attack(fire)
    pygame.display.update() 
  pygame.quit()

if __name__ == "__main__":
  main()
