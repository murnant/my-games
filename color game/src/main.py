import pygame
import random

clock = pygame.time.Clock()
screen = pygame.display.set_mode ((1000, 650),0,32)

mouse_x, mouse_y = pygame.mouse.get_pos()
hitbox = pygame.Rect(500, 250, 35, 35)


speed = 5
v_x = 0
v_y = 0
player_turn = True





spawnning = True

pygame.init()

spawn_x = -50
spawn_y = 0

hp = 99999

screen_border_Y = pygame.Rect(0, 0, 1000, 1)
screen_border_Y2 = pygame.Rect(0, 651, 1000, 1)
screen_border_Y3 = pygame.Rect(0, 0, 1, 650)
screen_border_Y4 = pygame.Rect(999, 0, 1, 650)

class Enemy():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.v_x = 0
        self.v_y = 0
        self.color = [255,255,0]
        self.color_stage = 0
        self.boom_timer = 247
        self.hitbox = pygame.Rect(self.x, self.y, 35, 35)
        

    def update(self, screen):
        if self.hitbox.colliderect(hitbox):
            self.v_x = v_x * 99
            self.v_y += v_y * 99
        self.v_x *= 0.09
        self.v_y *= 0.09
        self.x += self.v_x
        self.y += self.v_y
        self.boom_timer -= 1
        if self.boom_timer <=0:
            self.y += random.randint(-100,100)
            self.x += random.randint(-100,100)
            self.boom_timer = 247
            
        if self.hitbox.colliderect(screen_border_Y):
            self.y = 614
        if self.hitbox.colliderect(screen_border_Y2):
            self.y = 1
        if self.hitbox.colliderect(screen_border_Y3):
            self.x = 963
        if self.hitbox.colliderect(screen_border_Y4):
            self.x = 1
        self.hitbox = pygame.Rect(self.x, self.y, 35, 35)
        #color code
        if self.color == [0,0,0]:
            self.color_stage += 1
        if self.color == [255,255,255]:
            self.color_stage += 1
        if self.color == [255,255,0]:
            self.color_stage = 0
        if self.color_stage == 0:
            for c in range (3):
                if self.color[c] > 0:
                    self.color[c] -= 1
        if self.color_stage == 1:
            for c in range (3):
                if self.color[c] < 255:
                    self.color[c] += 1
        if self.color_stage == 2:
            for c in range (3):
                if self.color[c] > 0:
                    self.color[c] -= 1
        if self.color_stage == 3:
            for c in range (2):
                if self.color[c] < 255:
                    self.color[c] += 1
        pygame.draw.rect(screen, tuple(self.color), self.hitbox)
        if hitbox.x >= self.x:
            self.v_x += random.randint(1 + self.color_stage, 10 + self.color_stage) * 2

        if hitbox.x <= self.x:
            self.v_x -= random.randint(1 + self.color_stage, 10 + self.color_stage) * 2
                
        if hitbox.y <= self.y:
            self.v_y -= random.randint(1 + self.color_stage, 10 + self.color_stage) * 2

        if hitbox.y >= self.y:
            self.v_y += random.randint(1 + self.color_stage, 10 + self.color_stage) * 2

score = -10
color_timer_max = 200               
color_timer = -1

enemies = []
running = True

while spawnning:
    spawn_x += 50
    if spawn_x >= 1000:
        spawn_x = 10
        spawn_y += 50
    #if spawn_x == 70:
    enemies.append(Enemy(spawn_x, spawn_y))
    #else:
        #enemies.append(Enemy(spawn_x, spawn_y, 1))
    if spawn_y >= 650:
        spawnning = False


while hp >= 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if running:
        color_timer -= 1
        if color_timer <= 0:
            screen.fill((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))
            score += 10
            color_timer = color_timer_max

        if player_turn and pygame.mouse.get_pressed()[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if hitbox.x > mouse_x:
                v_x += -speed
                
            if hitbox.x < mouse_x:
                v_x += speed
                
            if hitbox.y < mouse_y:
                v_y += speed
                
            if hitbox.y > mouse_y:
                v_y += -speed



                
        v_x*= 0.3
        v_y*= 0.3
        hitbox.x += v_x
        hitbox.y += v_y





        if hitbox.colliderect(screen_border_Y):
            hitbox.y = 614
        if hitbox.colliderect(screen_border_Y2):
            hitbox.y = 20
        if hitbox.colliderect(screen_border_Y3):
            hitbox.x = 963
        if hitbox.colliderect(screen_border_Y4):
            hitbox.x = 1


        
                
            

        
        pygame.draw.rect(screen, (0, 255, 50), hitbox)

        #pygame.draw.rect(screen, (70, 70, 70), p2_hitbox)







        for enemy in enemies:
            enemy.update(screen)
            if enemy.hitbox.colliderect(hitbox) and not score == 0:
                hp -= 1


        pygame.display.update() # finally pushes changes to the screen

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        running = True
    
    clock.tick(50)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()) + " SCORE: " + str(score) + " HP: " + str(hp))

            

