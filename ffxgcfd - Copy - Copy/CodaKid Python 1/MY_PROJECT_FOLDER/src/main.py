import pygame
import random

# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
running = True

clock = pygame.time.Clock()
class Block():
    def __init__(self, x, y):
        self.size = 50
        self.hp = self.size *10
        self.hitbox = pygame.Rect(x, y, self.size, self.size)
        self.pic = pygame.image.load("../assets/block.png")
        self.pic_small = pygame.transform.scale(self.pic, (self.size, self.size))
        self.pic_small.set_colorkey((255,255,255))





class Fire():
    def __init__(self, x, y):
        self.fall = 1
        self.pic = pygame.image.load("../assets/Untitled.png")
        self.pic_small = pygame.transform.scale(self.pic, (50, 50))
        self.pic_small.set_colorkey((255,255,255))
        self.hitbox = pygame.Rect(x, y, 50, 50)


    def update(self, screen):
        self.fall += 0.1
        self.hitbox.y += self.fall
        screen.blit(self.pic_small, (self.hitbox.x, self.hitbox.y))

boom = True

timer = 0
spon_timer = 50

class Enemy():
    def __init__(self, x, y):
        self.moving = True
        if random.randint(1, 10) == 1:
            self.size = random.randint(50, 150)
        else:
            self.size = 50
        self.hp = self.size *10
        self.hitbox = pygame.Rect(x, y, self.size, self.size)
        self.pic = pygame.image.load("../assets/zom.png")
        self.pic_small = pygame.transform.scale(self.pic, (self.size, self.size))
        self.pic_small.set_colorkey((255,255,255))


    def update(self, screen):
        for block in blocks:
            if block.hitbox.colliderect(self.hitbox):
                self.moving = False
                block.hp -= 1
                if block.hp <= 0:
                    blocks.remove(block)
            else:
                self.moving = True

            screen.blit(block.pic_small, (block.hitbox.x, block.hitbox.y))

        if self.moving:
            self.hitbox.y -= 1
            if player_hitbox.x >= self.hitbox.x:
                self.hitbox.x += 1

            if player_hitbox.x <= self.hitbox.x:
                self.hitbox.x -= 1

            
        screen.blit(self.pic_small, (self.hitbox.x, self.hitbox.y))

    def ouch(self,damage):
        if self.hitbox.colliderect(boom_player_hitbox):
            self.hp -= damage *5
        if self.hitbox.colliderect(fire.hitbox):
            self.hp -= damage
            
        
        


player_hitbox = pygame.Rect(0, 0, 100, 100)
player_pic = pygame.image.load("../assets/car.png")
player_pic_small = pygame.transform.scale(player_pic, (100, 100))
player_pic_small.set_colorkey((255,255,255))

mouse_x, mouse_y = pygame.mouse.get_pos()
Fires = []
Enemys = []
blocks = []
Fires.append(Fire(mouse_x -20, 75))
boom_player_hitbox = pygame.Rect(-80, -80, 80, 80)
boom_pic = pygame.image.load("../assets/boom.png")
boom_pic_small = pygame.transform.scale(boom_pic, (80, 80))
boom_pic_small.set_colorkey((255,255,255))
block_timer = 0
background_pic = pygame.image.load("../assets/background.png")
background_pic_small = pygame.transform.scale(background_pic, (game_width, game_height))

living = True
score = 0

while living:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        running = True

    if not living:
        pygame.display.set_caption("GAME OVER :( our score: " + str(score))
            
    # ***************** Loop Land Below *****************
    # Everything under 'while running' will be repeated over and over again
    if running and living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.blit(background_pic_small, (0, 0))
        screen.blit(boom_pic_small, (boom_player_hitbox.x, boom_player_hitbox.y))
        screen.blit(player_pic_small, (player_hitbox.x, player_hitbox.y))

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if player_hitbox.x >= mouse_x -50:
            player_hitbox.x -= 9
        if player_hitbox.x <= mouse_x -50:
            player_hitbox.x += 9


        spon_timer -= 1
        if spon_timer <= 0:
            Enemys.append(Enemy(random.randint(0, game_width), game_height))
            spon_timer = 50
        
        keys = pygame.key.get_pressed()

        block_timer -= 1
        if pygame.mouse.get_pressed()[0] and block_timer <= 0:
            blocks.append(Block(mouse_x, mouse_y))
            block_timer = 800
        
        for fire in Fires:
            fire.update(screen)


        if boom and keys[pygame.K_SPACE]:
            Fires.append(Fire(player_hitbox.x +22.5, 75))
            boom = False
            timer = 21
        if timer >= 1 and not timer == 1:
            timer -= 1
        if timer == 1 and keys[pygame.K_SPACE]:
            boom_player_hitbox.x = fire.hitbox.x -17.5
            boom_player_hitbox.y = fire.hitbox.y -17.5
            Fires.remove(fire)
            boom = True
            timer = 0


            
        for enemy in Enemys:
            enemy.update(screen)
            enemy.ouch(1)
            if enemy.hitbox.y <= -enemy.size:
                Enemys.remove(enemy)
            if enemy.hp <= 0:
                score += enemy.size /5
                Enemys.remove(enemy)
            if enemy.hitbox.colliderect(player_hitbox):
                Enemys.remove(enemy)
                living = False


        # Tell pygame to update the screen
        pygame.display.update()
        clock.tick(50)
        pygame.display.set_caption("MY GAME SCORE: " + str(score) + "   MY GAME fps: " + str(clock.get_fps()))

