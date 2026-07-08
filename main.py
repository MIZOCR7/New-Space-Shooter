import pygame
import random
import player


pygame.init()
pygame.mixer.init()

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
  game_over = False
  
  right = False
  left = False
  up = False
  down = False
  fire = False
  
  bullets = []
  meteors = []
  score = 0
  meteor_spawn_timer = 0
  
  font = pygame.font.Font(None, 36)
  
  try:
    pygame.mixer.music.load("audio/game_music.wav")
    pygame.mixer.music.play(-1)
    laser_sound = pygame.mixer.Sound("audio/laser.wav")
    explosion_sound = pygame.mixer.Sound("audio/explosion.wav")
    damage_sound = pygame.mixer.Sound("audio/damage.ogg")
  except:
    laser_sound = explosion_sound = damage_sound = None
  
  while run:
    screen.fill((0,0,0))
    clock.tick(FPS)
    
    drawing_stars()
    
    if not game_over:
      meteor_spawn_timer += 1
      if meteor_spawn_timer > 30:
        meteors.append(player.Meteor())
        meteor_spawn_timer = 0
    
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
        if event.key == pygame.K_SPACE and not game_over:
          new_bullet = ship.attack(screen, fire=True)
          if new_bullet:
            if laser_sound:
              laser_sound.play()
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
    
    if not game_over:
      for bullet in bullets[:]:
        bullet.update()
        bullet.draw(screen)
        
        if bullet.rect.bottom == 0:
          bullets.remove(bullet)
        
        for meteor in meteors[:]:
          if bullet.rect.colliderect(meteor.rect):
            bullets.remove(bullet)
            meteors.remove(meteor)
            if explosion_sound:
              explosion_sound.play()
            score += 10
            break
      
      for meteor in meteors[:]:
        meteor.update()
        meteor.draw(screen)
        
        if meteor.rect.top > 720:
          meteors.remove(meteor)
        
        if ship.space_ship_rect.colliderect(meteor.rect):
          if damage_sound:
            damage_sound.play()
          game_over = True
      
      ship.draw(screen)
      ship.move(right, left, up, down) 
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    if game_over:
      game_over_text = font.render("GAME OVER - ESC to Exit", True, (255, 0, 0))
      screen.blit(game_over_text, (400, 350))
    
    pygame.display.update() 
  pygame.quit()


if __name__ == "__main__":
  main()
