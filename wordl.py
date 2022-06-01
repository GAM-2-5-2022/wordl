import pygame
import random

f = open("words.txt","r")
words = f.readlines()
guess = 0
user_text = ''
render_text = ''
old_guess = ''
state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
temp_state = [0,0,0,0,0]

def check():
    global user_text
    global temp_state
    user_text = user_text.lower()
    print(user_text)
    print(answer)
    if len(user_text) < 5:
        return -1
##    elif user_text not in words:
##        return -1
    elif user_text == answer:
        temp_state[0:5] = 1
        return 1
    else:
        for i in range(5):
            j = words.index(answer)
            if user_text[i] in words[j]:
                if user_text[i] == words[j][i]:
                    temp_state[i] = 1
                else:
                    temp_state[i] = -1
            else:
                temp_state[i] = 2
        old_guess = user_text
        user_text = ''
        return 0

def update_state():
    global state
    global temp_state
    state[5*guess : 5*guess+4] = temp_state[0:5]


pygame.init()

logo = pygame.image.load("wordl32.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("wordl")
green = pygame.image.load("green.png")
yellow = pygame.image.load("yellow.png")
gray = pygame.image.load("gray.png")
border = pygame.image.load("border.png")



answer = random.choice(words)
print(answer)

font = pygame.font.Font(None,60)

screen = pygame.display.set_mode((350,390))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif (len(user_text) < 5) & (event.key != pygame.K_RETURN):
                user_text += event.unicode
            elif event.key == pygame.K_RETURN:
                guess += 1
                print(check())
                update_state()
            
    
    screen.fill((255,255,255))
    for i in range(5):
        for j in range(6):
            n = j*5 + i
            if state[n] == 0:
                screen.blit(border, (64*i + 15,64*j))
            elif state[n] == -1:
                screen.blit(yellow, (64*i + 15,64*j))
            elif state[n] == 1:
                screen.blit(green, (64*i + 15,64*j))
            else:
                screen.blit(gray, (64*i + 15,64*j))


    user_text = user_text.upper()
    render_text = ''
    for i in range(len(user_text)):
        render_text += user_text[i] + '   '
    surface = font.render(render_text, True, (0,0,0))
    screen.blit(surface, (33,64*guess+10))
    
    pygame.display.flip()

f.close()


