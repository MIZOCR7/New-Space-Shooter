import pygame

class Player():
  def __init__(self, x, y):
    self.speed = 14
    self.direction = 1
    
    self.space_ship = pygame.image.load("images/player.png").convert_alpha()
    self.space_ship_rect = self.space_ship.get_rect()
    self.space_ship_rect.center = (x, y)
    
  def draw(self, screen):
    screen.fill((0,0,0))
    screen.blit(self.space_ship, self.space_ship_rect)
    
  def move(self, right, left, up, down):
    dx = 0
    dy = 0
    
    if self.space_ship_rect.x + self.space_ship.get_width() - 50 >= 1200:
      right = False
    if self.space_ship_rect.x - 20 <= 0:
      left = False 
    if self.space_ship_rect.y - 25 <= 0:
      up = False 
    if self.space_ship_rect.y + 100 >= 720:
      down = False 
    
    if right:
      self.direction = 1
      dx += self.speed * self.direction
      
    elif left:
      self.direction = -1
      dx += self.speed * self.direction  
    
    if up:
      dy -= self.speed
    elif down:
      dy += self.speed 
    

    self.space_ship_rect.x += dx 
    self.space_ship_rect.y += dy
  
  def attack(self, fire):
    if fire:
      pass 
