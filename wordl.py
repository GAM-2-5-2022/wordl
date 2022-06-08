import pygame
import random

f = open("words.txt","r")
words = f.readlines()
guess = 0
user_text = ''
render_text = ''
old_guesses = []
state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
temp_state = [0,0,0,0,0]
end = False

def check():
    global user_text
    global temp_state
    global end
    global guess
    user_text = user_text.lower()
    if len(user_text) < 5:
        return -1
    elif user_text + '\n' not in words:
        return -1
    elif user_text + '\n' == answer:
        for i in range(5):
            temp_state[i] = 1
        end = True
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
        old_guesses.append(user_text)
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
endfont = pygame.font.Font(None,30)

screen = pygame.display.set_mode((350,390))
width = screen.get_width()
height = screen.get_height()

running = True
while running:

    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if end == False:
            if event.type == pygame.KEYDOWN:
                if end == False:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif (len(user_text) < 5) & (event.key != pygame.K_RETURN):
                        user_text += event.unicode
                    elif event.key == pygame.K_RETURN:
                        if check() == 0:
                            print(check())
                            update_state()
                            guess += 1
                        elif check() != -1:
                            print(check())
                            update_state()
                        
        elif end == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/3 <= mouse[0] <= 2*width/3 and 2*height/5 >= mouse[1] >= height/5:
                    state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    old_guesses = []
                    user_text = ''
                    end = False
                    guess = 0
                    answer = random.choice(words)
                    print(answer)
                if width/3 <= mouse[0] <= 2*width/3 and 4*height/5 >= mouse[1] >= 3*height/5:
                    pygame.quit()
        
        if event.type == pygame.QUIT:
                pygame.quit()
            
    
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

    if len(old_guesses) > 0:
        for i in range(len(old_guesses)):
            render_text = ''
            for j in range(5):
                render_text += old_guesses[i][j] + '   '
            render_text = render_text.upper()
            old = font.render(render_text, True, (0,0,0))
            screen.blit(old, (33,64*i+10))
    user_text = user_text.upper()
    render_text = ''
    for i in range(len(user_text)):
        render_text += user_text[i] + '   '
    surface = font.render(render_text, True, (0,0,0))
    screen.blit(surface, (33,64*guess+10))

    if end == True:
        if width/3 <= mouse[0] <= 2*width/3 and 2*height/5 >= mouse[1] >= height/5:
            pygame.draw.rect(screen,(170,170,170),[width/3,height/5,width/3,height/5])
              
        else:
            pygame.draw.rect(screen,(100,100,100),[width/3,height/5,width/3,height/5])

        if width/3 <= mouse[0] <= 2*width/3 and 4*height/5 >= mouse[1] >= 3*height/5:
            pygame.draw.rect(screen,(170,170,170),[width/3,3*height/5,width/3,height/5])
              
        else:
            pygame.draw.rect(screen,(100,100,100),[width/3,3*height/5,width/3,height/5])
        gameover = font.render("GAME OVER", True, (0,0,0))
        screen.blit(gameover, (width/7, 4*height/9))
        play = endfont.render("PLAY", True, (255,255,255))
        screen.blit(play, (0.42*width, 0.25*height))
        again = endfont.render("AGAIN", True, (255,255,255))
        screen.blit(again, (0.4*width, 0.3*height))
        ex = endfont.render("EXIT", True, (255,255,255))
        screen.blit(ex, (0.42*width,0.67*height))

        
    pygame.display.flip()

f.close()


