import pygame
import random

clock = pygame.time.Clock()
screen = pygame.display.set_mode ((1000, 650),0,32)

x = 1000
y = 0
speed = 20
down = True

class Enemy():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.hitbox = pygame.Rect(self.x, self.y, 35, 35)
        self.show_x = True
        self.show_y = True


    def update(self, screen):
        self.hitbox.y += self.speed
        if x > 1000 and self.hitbox.x > 500:
            self.show_x = True
        else:
            if x <= 0 and self.hitbox.x < 500:
                self.show_x = True
            else:
                self.show_x = False


        if y > 1000 and self.hitbox.y > 325:
            self.show_y = True
        else:
            if y <= 0 and self.hitbox.y < 325:
                self.show_y = True
            else:
                self.show_y = False

        if self.show_x and self.show_y:
            pygame.draw.rect(screen, (70, 255, 70), self.hitbox)


enimies = [Enemy(378, 0, 1)]

pygame.init()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))

    pygame.draw.line(screen, (70,255,70), (500,325), (x,y), 10)
    if y < 650 and down:
        y += speed
        x = 1000
    else:
        if x >= 0 and down:
            x -= speed
            y = 650
        else:
            if y <= 0:
                x += speed
                y = 0
                if x >= 1000:
                    down = True
            else:
                down = False
                y -= speed
                x = 0

    for enemy in enimies:
        enemy.update(screen)

    pygame.display.update() # finally pushes changes to the screen

    clock.tick(20)
