import pygame
import os

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
class Enemy():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.v_x = 0
        self.v_y = 0
        self.hitbox = pygame.Rect(self.x, self.y, w, h)
        

    def update(self, screen):
        pygame.draw.rect(screen, (153, 76, 0), self.hitbox)


enemy_hitbox_v_x =0
enemy_hitbox_v_y =0
spawnning = True
spawn_x = -10
spawn_y = 400
player = pygame.Rect(0, 100, 40, 40)
player_v_x = 0
bounce = 0.01
enemy_down = False
up_and_down_timer = 600
falling_on = True
enemies = []
enemy_hitbox = pygame.Rect(900, 620, 85, 85)
while spawnning:
    spawn_x += 10
    if spawn_x >= 1000:
        spawn_x = 0
        spawn_y += 10
    enemies.append(Enemy(spawn_x, spawn_y, 10, 10))
    if spawn_y >= 650:
        spawnning = False
falling = 0
fall_stopper = pygame.Rect(0, 0,game_width , game_height)
tail_size = 99
tail_size_max = 0
land_shark = []
# ***************** Loop Land Below *****************
# Everything under 'while running' will be repeated over and over again
while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill((102, 51, 0))
    keys = pygame.key.get_pressed()
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255,255,0), enemy_hitbox)


    land_shark.append(enemy_hitbox.copy())
    tail_size_max += 1
    if tail_size_max >= 600:
        tail_size += 1
    
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_v_x += 3

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_v_x -= 3


    player_v_x *= 0.7
    player.x += player_v_x

    if player.x >= enemy_hitbox.x:
        enemy_hitbox_v_x += 1

    if player.x <= enemy_hitbox.x:
        enemy_hitbox_v_x -= 1
                
    if player.y <= enemy_hitbox.y and not enemy_down:
        enemy_hitbox_v_y -= 1

    if player.y >= enemy_hitbox.y and not enemy_down:
        enemy_hitbox_v_y += 1
    if enemy_down:
        if up_and_down_timer ==0:
            up_and_down_timer = 600
            enemy_down = False
        else:
            up_and_down_timer -= 1
        enemy_hitbox_v_y += 1
    else:
        if up_and_down_timer ==0:
            land_shark.append(enemy_hitbox.copy())
            up_and_down_timer = 300
            enemy_down = True
        else:
            up_and_down_timer -= 1

    enemy_hitbox_v_x *= 0.7
    enemy_hitbox_v_y *= 0.7
    enemy_hitbox.x += enemy_hitbox_v_x
    enemy_hitbox.y += enemy_hitbox_v_y

    for i in range(10):
            
        
        if not fall_stopper.colliderect(player):
            falling *= -bounce
            player_v_x *= -bounce
            


        for enemy in enemies:
            if enemy.hitbox.colliderect(enemy_hitbox):
                enemies.remove(enemy)
        for enemy in enemies:
            if enemy.hitbox.colliderect(player) and falling >= 0:
                if keys[pygame.K_SPACE]:
                    falling -= 1
                else:
                    falling_on = False
                    falling *= -bounce
                break

            else:
                falling_on = True


        for tail in range (tail_size_max):
            if tail >= tail_size:
                if tail >= len(land_shark) -20:
                    pygame.draw.rect(screen, (255,255,0), land_shark [tail])
                else:
                    pygame.draw.rect(screen, (240,240,0), land_shark [tail])
                if land_shark [tail].colliderect(player) and falling >= 0:
                    if keys[pygame.K_SPACE]:
                        falling -= 1
                    else:
                        falling_on = False
                        falling *= -bounce
                    break

                else:
                    falling_on = True
                    
                land_shark [tail].x += -enemy_hitbox_v_x /2
                land_shark [tail].y += -enemy_hitbox_v_y /2
                    
                for enemy in enemies:
                    if enemy.hitbox.colliderect(land_shark [tail]):
                        enemies.remove(enemy)


            

        
        if falling_on:
            falling += 0.01
                
        player.y += falling

        #Tell pygame to update the screen
    for enemy in enemies:
        enemy.update(screen)
    pygame.display.update()
    clock.tick(999999999999999999999)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
