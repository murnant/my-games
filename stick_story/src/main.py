import pygame
import os

y = 0
i = 0
current_choice = 2
story = "aba"
game = True
# Start the game
pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True


animation = []
path = "../assets/test2/"
files = os.listdir(path)
for f in files:
    temp = pygame.image.load(path + f)
    animation.append(temp)
  

def load_choice(current_choice):
    choices = []
    path = "../assets/"+str(current_choice)+"/"
    files = os.listdir(path)
    for f in files:
        temp = pygame.image.load(path + f)
        temp_small = pygame.transform.scale(temp, (100, 100))
        choices.append(temp_small)
    return choices


choices = load_choice(current_choice)


#pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR) #->

while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
    screen.fill((0,0,0))
    
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if i < len(animation) -1:
        i += 1
    elif not game:
        running = False
    screen.blit(animation[i],(0 , 0))

    #y = 0
    x = 600
    if pygame.mouse.get_pressed()[0] and mouse_x > x and mouse_x < x +100 and mouse_y < y+100 and mouse_y > y and not i < len(animation) -1:
            current_choice += 1
            i = 1
            animation = []
            path = "../assets/test"+str(current_choice)+"a/"
            files = os.listdir(path)
            for f in files:
                temp = pygame.image.load(path + f)
                #temp.set_colorkey((255,255,255))
                animation.append(temp)
            #y += 200
            choices = load_choice(current_choice)
            if story[current_choice -2] == "a":
                game = False
            
    for img in choices:
        screen.blit(img,(x , y))
        x += 200
        if pygame.mouse.get_pressed()[0] and mouse_x > x and mouse_x < x +100 and mouse_y < y+100 and mouse_y > y and not i < len(animation) -1:
            current_choice += 1
            i = 1
            animation = []
            path = "../assets/test"+str(current_choice)+"b/"
            files = os.listdir(path)
            for f in files:
                temp = pygame.image.load(path + f)
                #temp.set_colorkey((255,255,255))
                animation.append(temp)
            #y += 200
            choices = load_choice(current_choice)
            if story[current_choice -2] == "b":
                game = False
             
        
    

    # Tell pygame to update the screen
    pygame.display.flip()
    clock.tick(30)
    pygame.display.set_caption("MY GAME fps: " + str(clock.get_fps()))
