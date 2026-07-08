import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")

surf = pygame.Surface((100,200))
surf.fill("red")

player_surf = pygame.image.load("images/player.png")

def main():
  run = True

  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False 
      
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          run = False
    
    screen.fill('darkgray')
    screen.blit(player_surf, (100,150))
    pygame.display.update() 
  pygame.quit()

if __name__ == "__main__":
  main()
