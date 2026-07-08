import pygame
import random
import player


pygame.init()

WIDTH = 1280
HEIGHT = 720
FPS = 60

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Shooter")

ship = player.Player(100,200)

stars_pos = []
for _ in range(10):
  star_x = random.randint(10, 1270)
  star_y = random.randint(10,710)
  stars_pos.append((star_x, star_y))
star_img = pygame.image.load("images/star.png").convert_alpha()
star_rect = star_img.get_rect()

def drawing_stars():
  for pos in stars_pos:
    star_rect.center = pos
    screen.blit(star_img, star_rect)

def main():
  run = True
  
  right = False
  left = False
  up = False
  down = False
  fire = False
  
  bullets = []
  
  while run:
    screen.fill((0,0,0))
    clock.tick(FPS)
    
    drawing_stars()
    
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
        if event.key == pygame.K_SPACE:
          new_bullet = ship.attack(screen, fire=True)
          if new_bullet:
            bullets.append(new_bullet)
      
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
          right = False
        if event.key == pygame.K_a:
          left = False 
        if event.key == pygame.K_w:
          up = False
        if event.key == pygame.K_s:
          down = False
      
    for bullet in bullets[:]:
      bullet.update()
      bullet.draw(screen)
      
      if bullet.rect.bottom == 0:
        bullets.remove(bullet)
    
    ship.draw(screen)
    ship.move(right, left, up, down) 
    ship.attack(screen, fire)
    pygame.display.update() 
  pygame.quit()

if __name__ == "__main__":
  main()
