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

    def __str__():
        return "(" + self.x + "," + self.y + ")"


class Snake():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)
        self.tail = [P(x,y),P(x+1,y),P(x +1,y +1)]
        

    def update(self, screen,x,y,food):

        
        
        if not x == 0 or not y == 0:
            self.x += x
            self.y += y
            self.tail.append(P(self.x,self.y))
            print(self.x,self.y)
        # eat food
        for f in food:
            if f.x == self.x and f.y == self.y:
                # remove food
                food.remove(f)
                # don't remove end of tail (grow)
            elif not x == 0 or not y == 0:
                # delete end of tail
                self.tail.pop(0)     #pop() opposite of append. pop(0) removes the first element
                

    def draw(self,screen):
        for t in self.tail:
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(t.x *47,t.y *47,47,47))


player = Snake(5,5)

food = [P(2,2),P(5,5)]

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


    for f in food:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(f.x *47,f.y *47,47,47))

    player.update(screen,v_x,v_y, food)
    player.draw(screen)

    v_x = 0
    v_y = 0

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        v_x = 1

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        v_x = -1
    if keys[pygame.K_UP] or keys[pygame.K_w]: 
        v_y = -1

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        v_y = 1



    pygame.display.update()
    clock.tick(5)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))



