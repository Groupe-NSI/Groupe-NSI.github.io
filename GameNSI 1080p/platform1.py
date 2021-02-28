import pygame
import random


class Platform(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.v = 0
        self.velocity = 2
        self.image = pygame.image.load("assets/platform.png")
        self.rect = self.image.get_rect()
        self.rect.x = 75 * random.randrange(26, 52)
        self.rect.y = 5 + 75 * random.randrange(0, 14)

    def update(self, surface):
        self.rect.x -= self.velocity + self.v
        self.v += 0.002
        if self.rect.right <= 0:
            self.rect.x += 1995
            self.rect.y = 5 + 75 * random.randrange(0, 14)

        surface.blit(self.image, self.rect)


class Rp(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.velocity = 2
        self.v = 0
        self.image = pygame.image.load("assets/redplatform.png")
        self.rect = self.image.get_rect()
        self.rect.x = 75 * random.randrange(26, 52)
        self.rect.y = 5 + 75 * random.randrange(0, 14)

    def update(self, surface):
        self.rect.x -= self.velocity + self.v
        self.v += 0.002
        if self.rect.right <= 0:
            self.rect.x += 1995
            self.rect.y = 5 + 75 * random.randrange(0, 14)
        surface.blit(self.image, self.rect)


class Player1(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.all_platforms = pygame.sprite.Group()
        self.all_rp = pygame.sprite.Group()
        self.velocity = 3
        self.v = 1
        self.image = pygame.image.load('assets/player1.png')
        self.rect = self.image.get_rect()
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

    def redCollision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

    def Movements(self):
        collision_type = {'RIGHT': False, 'LEFT': False, 'TOP': False, 'BOTTOM': False, 'FLOOR': True}
        for platform in self.all_platforms:
            if self.rect.colliderect(platform.rect):
                if abs(self.rect.bottom - platform.rect.top) < 7 and self.mj > 0:
                    self.rect.bottom = platform.rect.top
                    collision_type['BOTTOM'] = True
                elif self.rect.right - platform.rect.left < self.collision_tolerance:
                    collision_type['RIGHT'] = True
                    self.rect.right = platform.rect.left
                elif abs(self.rect.left - platform.rect.right) < self.collision_tolerance:
                    self.rect.left = platform.rect.right - 2
                    collision_type['LEFT'] = True
                elif abs(self.rect.top - platform.rect.bottom) < self.collision_tolerance + 100:
                    collision_type['TOP'] = True
                    self.isJumping = False
            if not abs(self.rect.y - 985) < self.collision_tolerance:
                collision_type['FLOOR'] = False
        self.mj = 0
        pressed_keys = pygame.key.get_pressed()
        self.velocity = 3 + self.v
        self.collision_tolerance = 7 + self.v ** 2
        if self.rect.right < 1920 and pressed_keys[pygame.K_d] and not collision_type['RIGHT']:
            self.mx += self.velocity
        if self.rect.left > 0 and pressed_keys[pygame.K_a] and not collision_type['LEFT']:
            self.mx -= self.velocity
        if pressed_keys[pygame.K_SPACE] and (collision_type['BOTTOM'] or collision_type['FLOOR']):
            self.isJumping = True
            self.jumpCount = 120
            self.jumpStatus = 4
        if self.isJumping and self.jumpCount > 0 and not collision_type['TOP']:
            self.jumpStatus = -0.00125 * self.jumpCount ** 2
            self.my += self.jumpStatus
            self.jumpCount -= 1
        elif self.isJumping and self.jumpCount == 0 and self.rect.y == 1055 - self.image.get_height():
            self.isJumping = False
        if collision_type['TOP']:
            self.my = 0
        if self.rect.y >= 1055 - self.image.get_height():
            self.rect.y = 1055 - self.image.get_height()
        else:
            self.my += 5
        self.v += 0.002
        self.mj = self.my
        self.rect.move_ip(self.mx, self.my)
        self.mx = 0
        self.my = 0
