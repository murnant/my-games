import pygame
# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
v_x = 0
v_y = 0
class P(object):
    '''Creates a point on a coordinate plane with values x and y.'''

    def __init__(self, x, y):
        '''Defines x and y variables'''
        self.x = x
        self.y = y


class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)
        self.tail = [P(x,y),P(x +47,y),P(x +47,y +47)]
        

    def update(self, screen,x,y):
        for t in self.tail:
            t.x += x
            t.y += y
        pygame.draw.rect(screen, (153, 76, 0), self.hitbox)


    def draw(self,screen):
        for t in self.tail:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(t.x,t.y,47,47))


player = Snake(50,50)

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


    player.update(screen,v_x,v_y)
    player.draw(screen)


    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        v_x = 47

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        v_x = -47



    pygame.display.update()
    clock.tick(5)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
