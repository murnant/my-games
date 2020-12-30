import pygame
import random

clock = pygame.time.Clock()
screen = pygame.display.set_mode ((1000, 500),0,32)

pygame.init()
player_hitbox = pygame.Rect(100, 100,10,10)
zom = 50
running = True
#maze_pic = pygame.image.load("../assets/maze.png")
#maze_pic_small = pygame.transform.scale(maze_pic, (5000, 2500))
walls =[]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
    screen.fill((100,100,100))


    #screen.blit(maze_pic_small, (x, y))


    mouse_x, mouse_y = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        zom += 0.1
    if keys[pygame.K_j]:
        zom -= 0.1

    if pygame.mouse.get_pressed()[0]:
        walls.append(pygame.Rect(mouse_x, mouse_y,10 +zom,10 +zom))
    for w in walls:
        if keys[pygame.K_RIGHT]:
            w.x -= 3
        if keys[pygame.K_LEFT]:
            w.x += 3
        if keys[pygame.K_UP]:
            w.y += 3
        if keys[pygame.K_DOWN]:
            w.y -= 3


        w.width = 10 +zom
        w.height = 10 +zom
        if w.colliderect(player_hitbox):
            running=False
                
        pygame.draw.rect(screen, (255, 0, 0), w)

    if running:
        pygame.draw.rect(screen, (255, 255, 255), player_hitbox)

    pygame.display.update() # finally pushes changes to the screen
