import pygame
import pygame_textinput
clock = pygame.time.Clock()
screen = pygame.display.set_mode ((1000, 650),0,32)
textinput = pygame_textinput.TextInput(text_color =(255,255,255))

class Shell():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.v_x = 1
        self.v_y = -1
        self.hitbox = pygame.Rect(self.x, self.y, w, h)
        

    def update(self, screen):
        self.v_y += 0.1
        self.hitbox.y += self.v_y
        self.hitbox.x += self.v_x
        pygame.draw.rect(screen, (255, 255, 255), self.hitbox)


class Ground_Tile():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, w, h)
        

    def update(self, screen):
        pygame.draw.rect(screen, (153, 76, 0), self.hitbox)

class Ground():
    def __init__(self,w, h, tile_size):
        spawn_x = -tile_size
        spawn_y = 400
        self.tiles =[]
        while spawn_y <= h:
            spawn_x += tile_size
            if spawn_x >= w:
                spawn_x = 0
                spawn_y += tile_size
            self.tiles.append(Ground_Tile(spawn_x, spawn_y, tile_size, tile_size))
        

    def update(self, screen):
        for t in self.tiles:
            t.update(screen)

ground = Ground(1000,650,10)

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



    screen.fill((0,0,0))

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




