import pygame
import random


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 2
        self.image = pygame.image.load("assets/platform3d.png")
        self.rect = pygame.Rect(0, 0, 75, 75)
        self.rect.x = 75 * random.randrange(26, 52)
        self.rect.y = 55 + 75 * random.randrange(0, 12)

    def update(self, surface):
        self.rect.x -= self.velocity
        if self.rect.right <= 0:
            self.rect.x += 1995
            self.rect.y = 55 + 75 * random.randrange(0, 12)
        surface.blit(self.image, self.rect)


class Rp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 2
        self.image = pygame.image.load("assets/rp3d.png")
        self.rect = pygame.Rect(0, 0, 75, 75)
        self.rect.x = 75 * random.randrange(26, 52)
        self.rect.y = 55 + 75 * random.randrange(0, 12)

    def update(self, surface):
        self.rect.x -= self.velocity
        if self.rect.right <= 0:
            self.rect.x += 1995
            self.rect.y = 55 + 75 * random.randrange(0, 12)
        surface.blit(self.image, self.rect)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.velocity = 2
        self.image = pygame.image.load("assets/coin3d.png")
        self.rect = pygame.Rect(0, 0, 75, 75)
        self.rect.x = 75 * random.randrange(26, 52)
        self.rect.y = 55 + 75 * random.randrange(0, 12)

    def update(self, surface):
        self.rect.x -= self.velocity
        if self.rect.right <= 0:
            self.rect.x += 1995
            self.rect.y = 55 + 75 * random.randrange(0, 12)
        surface.blit(self.image, self.rect)


class Player1(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.all_platforms = pygame.sprite.Group()
        self.all_rp = pygame.sprite.Group()
        self.all_coins = pygame.sprite.Group()
        self.velocity = 3
        self.v = 1
        self.image = pygame.image.load('assets/player3d.png')
        self.rect = pygame.Rect(0, 0, 75, 75)
        self.rect.y = 1055
        self.rect.x = 25
        self.isJumping = False
        self.mx, self.my, self.mj = 0, 0, 0
        self.jumpCount = 120
        self.jumpStatus = 4
        self.collision_tolerance = 7

    def spawn_platforms(self):
        self.all_platforms.add(Platform())

    def spawn_redplatforms(self):
        self.all_rp.add(Rp())

    def spawn_coins(self):
        self.all_coins.add(Coin())

    def Collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def Movements(self):
        hit_list = []
        for platform in self.all_platforms:
            if self.rect.colliderect(platform.rect):
                hit_list.append(platform)
        self.collision_type = {'RIGHT': False, 'LEFT': False, 'TOP': False, 'BOTTOM': False, 'FLOOR': True}
        for platform in hit_list:
            if abs(self.rect.bottom - platform.rect.top) < 7 and self.mj > 0:
                self.rect.bottom = platform.rect.top
                self.collision_type['BOTTOM'] = True
            elif abs(self.rect.right - platform.rect.left) < self.collision_tolerance:
                self.rect.right = platform.rect.left
                self.collision_type['RIGHT'] = True
            elif abs(self.rect.left - platform.rect.right) < self.collision_tolerance:
                self.rect.left = platform.rect.right + 1
                self.collision_type['LEFT'] = True
            elif abs(self.rect.top - platform.rect.bottom) < self.collision_tolerance + 100:
                self.rect.top = platform.rect.bottom
                self.collision_type['TOP'] = True
                self.isJumping = False
        if not abs(self.rect.y - 955) < self.collision_tolerance:
            self.collision_type['FLOOR'] = False
        self.mj = 0
        pressed_keys = pygame.key.get_pressed()
        self.collision_tolerance = 7 + self.v ** 2
        if self.rect.right < 1920 and pressed_keys[pygame.K_d] and not self.collision_type['RIGHT']:
            self.mx += self.velocity
        if self.rect.left > 0 and pressed_keys[pygame.K_a]:
            self.mx -= self.velocity
        if pressed_keys[pygame.K_SPACE] and (self.collision_type['BOTTOM'] or self.collision_type['FLOOR']):
            self.isJumping = True
            self.jumpCount = 120
            self.jumpStatus = 4
        if self.isJumping and self.jumpCount > 0 and not self.collision_type['TOP']:
            self.jumpStatus = -0.0013 * self.jumpCount ** 2
            self.my += self.jumpStatus
            self.jumpCount -= 1
        elif self.isJumping and self.jumpCount == 0 and self.rect.y == 955:
            self.isJumping = False
        if self.collision_type['TOP']:
            self.my = 0
        if self.rect.y >= 1055 - self.image.get_height():
            self.rect.y = 1055 - self.image.get_height()
        else:
            self.my += 5
        self.mj = self.my
        self.rect.move_ip(self.mx, self.my)
        self.mx = 0
        self.my = 0
