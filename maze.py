import pygame
import random

clock = pygame.time.Clock()
screen = pygame.display.set_mode ((1000, 500),0,32)

class Wall():
    def __init__(self, x, y,size):
        self.hitbox = pygame.Rect(x, y, size, size)
        self.start_x = 0
        self.start_y = 0

pygame.init()
player_hitbox = pygame.Rect(500, 250,10,10)
zom = 50
running = True
start = False
#maze_pic = pygame.image.load("../assets/maze.png")
#maze_pic_small = pygame.transform.scale(maze_pic, (5000, 2500))
walls =[]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if start:
                for w in walls:
                    w.hitbox.x = w.start_x
                    w.hitbox.y = w.start_y
                else:
                    running = True
    screen.fill((100,100,100))


    #screen.blit(maze_pic_small, (x, y))


    mouse_x, mouse_y = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        zom += 1
    if keys[pygame.K_j]:
        zom -= 1

    if pygame.mouse.get_pressed()[0] and not start:
        if keys[pygame.K_SPACE]:
            for w in walls:
                w.start_x = w.hitbox.x
                w.start_y = w.hitbox.y
            player_hitbox = pygame.Rect(mouse_x, mouse_y,10,10)
            start = True
        else:
            walls.append(Wall(mouse_x, mouse_y,zom))
    for w in walls:
        if keys[pygame.K_RIGHT]:
            w.hitbox.x -= 3
        if keys[pygame.K_LEFT]:
            w.hitbox.x += 3
        if keys[pygame.K_UP]:
            w.hitbox.y += 3
        if keys[pygame.K_DOWN]:
            w.hitbox.y -= 3


        w.hitbox.width = zom
        w.hitbox.height = zom
        if w.hitbox.colliderect(player_hitbox) and start:
            for w in walls:
                w.hitbox.x = w.start_x
                w.hitbox.y = w.start_y
                
        pygame.draw.rect(screen, (255, 0, 0), w.hitbox)

    if start:
        pygame.draw.rect(screen, (255, 255, 255), player_hitbox)

    pygame.display.update() # finally pushes changes to the screen
