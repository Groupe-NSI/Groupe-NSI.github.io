import pygame
from platform1 import Player1
from platform1 import Platform
from platform1 import Rp
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Marseille 2021")
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('assets/background.png')
bm = pygame.image.load('assets/backgroundm.png')
playerg = pygame.image.load('assets/player1.png')
playerb = pygame.image.load('assets/playerb.png')
playerj = pygame.image.load('assets/playerj.png')
playerm = pygame.image.load('assets/playerm.png')
playern = pygame.image.load('assets/playern.png')

mixer.music.load('assets/music.mp3')
mixer.music.play(-1)
star = pygame.transform.scale(pygame.image.load("assets/star.png"), (screen_height // 2, screen_height // 2))
toad = pygame.transform.scale(pygame.image.load("assets/toad.png"), (screen_height // 2, screen_height // 2))
starx = screen_width
toadx = screen_width
player1 = Player1()
platform = Platform()
rp = Rp()
running = True
menu = True
playing = False
settings = False
x = 0
pressed_keys = pygame.key.get_pressed()

for i in range(0, 40):
    player1.spawn_platforms()
for i in range(0, 15):
    player1.spawn_redplatforms()

pressed = {}

while running:
    while menu:
        screen.blit(bm, (0, 0))
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                menu = False
                playing = True
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    menu = False
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                sx, sy = pygame.mouse.get_pos()
                if 1500 < sx < 1829 and 920 < sy < 990:
                    menu = False
                    settings = True
        pygame.display.update()
    while settings:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    settings = False
                    menu = True
        pygame.display.update()
        screen.blit(background, (0, 0))
        pygame.mouse.set_visible(True)
        sx, sy = pygame.mouse.get_pos()
        playerg = pygame.transform.scale(playerg, (175, 175))
        playerj = pygame.transform.scale(playerj, (175, 175))
        playerm = pygame.transform.scale(playerm, (175, 175))
        playerb = pygame.transform.scale(playerb, (175, 175))
        playern = pygame.transform.scale(playern, (175, 175))
        screen.blit(playerg, (screen_width // 11, (screen_height - 175) // 2))
        screen.blit(playerj, (screen_width // 11 * 3, (screen_height - 175) // 2))
        screen.blit(playerm, (screen_width // 11 * 5, (screen_height - 175) // 2))
        screen.blit(playerb, (screen_width // 11 * 7, (screen_height - 175) // 2))
        screen.blit(playern, (screen_width // 11 * 9, (screen_height - 175) // 2))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 175 < sx < 350 and 453 < sy < 588:
                    player1.image = pygame.image.load('assets/player1.png')
                    settings = False
                    menu = True
                if 525 < sx < 700 and 453 < sy < 588:
                    player1.image = pygame.image.load('assets/playerj.png')
                    settings = False
                    menu = True
                if 875 < sx < 1050 and 453 < sy < 588:
                    player1.image = pygame.image.load('assets/playerm.png')
                    settings = False
                    menu = True
                if 1225 < sx < 1400 and 453 < sy < 588:
                    player1.image = pygame.image.load('assets/playerb.png')
                    settings = False
                    menu = True
                if 1575 < sx < 1750 and 453 < sy < 588:
                    player1.image = pygame.image.load('assets/playern.png')
                    settings = False
                    menu = True
    while playing:
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                game = False
            if event.type == pygame.KEYDOWN:
                pressed[event.key] = True
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    menu = True
        player1.Movements()
        screen.blit(background, (0, 0))
        screen.blit(star, (starx, 255))
        starx -= 0.5
        if starx < -300:
            screen.blit(toad, (toadx, 255))
            toadx -= 0.5
        if starx < -300 and toadx < -300:
            starx = 1920
            toadx = 1920
        player1.all_platforms.update(screen)
        player1.all_rp.update(screen)
        screen.blit(player1.image, player1.rect)
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed[event.key] = True
                if event.key == pygame.K_ESCAPE:
                    playing = False
                    menu = True
        if player1.redCollision(player1, player1.all_rp):
            for i in range(0, 1):
                player1.spawn_redplatforms()
            playing = False
            menu = True
        if player1.rect.right <= 0:
            player1.rect.x = 100
            playing = False
            menu = True
