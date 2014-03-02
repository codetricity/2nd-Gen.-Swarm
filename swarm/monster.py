import pygame
import random
        
class Monster(pygame.sprite.Sprite):
    def __init__(self, monster_type = "zombie"):
        ## use the line below in all sprite initialization
        pygame.sprite.Sprite.__init__(self)
        
        if monster_type == "zombie":
            self.image = pygame.image.load("img/monster_small.png").convert_alpha()
        if monster_type == "mummy":
            self.image = pygame.image.load("img/SuperMonster_mummy.png")
        elif monster_type == "crab":
            self.image = pygame.image.load("img/superMonster_crab.png")

        self.image.convert_alpha()

        self.rect = self.image.get_rect()

        if monster_type == "mummy" or monster_type == "crab":
            self.rect.center = (random.randint(400, 500), random.randint(150, 340))
            self.speed_trigger = 1
            self.current_trigger = 0

        
        self.safe_surf = pygame.Surface((480, 320))
        self.safe_zone = self.safe_surf.get_rect()
        self.safe_zone.center = (240, 160)
        
        self.in_safe = False
        while not self.in_safe:
            self.rect.right = random.randrange(480, 800)
            self.rect.top = random.randrange(-300, 0)
            if self.rect.colliderect(self.safe_zone):
                pass
            else:
                self.in_safe = True
        self.speed = 1

            
        
    
    def update(self, character, level):
        print(level)
    ####
        if level == 2:
            self.speed = 2
        if level == 3:
            self.speed = 2
        if level == 4:
            self.speed = 2
        if level == 5:
            self.speed = 3
        if level == 6:
            self.speed = 3
        if level == 7:
            self.speed = 3
        if level == 8:
            self.speed = 3
        
        self.char = character
        x = self.char.rect.centerx
        y = self.char.rect.centery
        if self.rect.centerx > x:
            self.rect.centerx -= self.speed
        if self.rect.centerx < x:
            self.rect.centerx += self.speed
        if self.rect.centery > y:
            self.rect.centery -= self.speed
        if self.rect.centery < y:
            self.rect.centery += self.speed
