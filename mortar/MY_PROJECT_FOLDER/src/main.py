import pygame
import pygame_textinput
import random
clock = pygame.time.Clock()
screen = pygame.display.set_mode ((1000, 650),0,32)
textinput = pygame_textinput.TextInput(text_color =(255,255,255))

class Shell():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = -h
        self.des = y
        self.blone_up = False
        self.w = w
        self.h = h
        self.v_x = 1
        self.v_y = -1
        self.pic = pygame.image.load("../assets/Untitled.png")
        self.pic_small = pygame.transform.scale(self.pic, (self.w, self.h))
        self.pic_small.set_colorkey((255,255,255))
        self.boom_pic = pygame.image.load("../assets/boom.jpg")
        self.boom_pic_small = pygame.transform.scale(self.boom_pic, (self.w +100, self.h +100))
        self.hitbox = pygame.Rect(self.x, self.y, w, h)
        

    def update(self, screen):
        if self.blone_up:
            screen.blit(self.boom_pic_small, (self.hitbox.x, self.hitbox.y))
        else:
            if self.hitbox.y < self.des:
                self.v_y += 0.1
                self.hitbox.y += self.v_y
            else:
                self.hitbox = pygame.Rect(self.hitbox.x -50, self.hitbox.y -50, self.w +100, self.w +100)
                self.blone_up = True
            
            screen.blit(self.pic_small, (self.hitbox.x, self.hitbox.y))


class Ground_Tile():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.pic = pygame.image.load("../assets/dert.png")
        self.pic_small = pygame.transform.scale(self.pic, (w, h))
        self.hitbox = pygame.Rect(self.x, self.y, w, h)
        

    def update(self, screen):
        screen.blit(self.pic_small, (self.hitbox.x, self.hitbox.y))
                



class Ground():
    def __init__(self,w, h, tile_size):
        spawn_x = -tile_size
        spawn_y = 400
        spawn_x2 = random.randint(1, 300)
        spawn_size = random.randint(1, 30)* tile_size + spawn_x2
        self.tiles =[]
        while spawn_y <= h:
            spawn_x += tile_size
            if spawn_x >= w:
                spawn_x = 0
                spawn_y += tile_size
            self.tiles.append(Ground_Tile(spawn_x, spawn_y, tile_size, tile_size))
        while not spawn_x2 == spawn_size:
            self.tiles.append(Ground_Tile(spawn_x2,spawn_y - tile_size, tile_size, tile_size))
            if random.randint(1, 5) == 1:
                spawn_x2 += tile_size
            else:
                spawn_y -= tile_size
            if random.randint(1, 7) == 1:
                spawn_x2 -= tile_size
        
        

    def update(self, screen):
        for t in self.tiles:
            t.update(screen)
            for s in shells:
                if s.hitbox.colliderect(t.hitbox):
                    self.tiles.remove(t)



ground = Ground(1000,650,50)

shells = []

running = True
while running:
    events = pygame.event.get()
    fire = False
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            fire = True



    screen.fill((100,100,255))

    ground.update(screen)
    if fire:
        x,y = textinput.get_text().split(",")
        shells.append(Shell(int(x),int(y), 75, 75))
    for s in shells:
        s.update(screen)



    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.get_surface(), (10, 10))


    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
    pygame.display.update()
    clock.tick(50)




