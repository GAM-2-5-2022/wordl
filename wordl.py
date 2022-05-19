import pygame

def main():
    pygame.init()

    logo = pygame.image.load("wordl32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("wordl")

    green = pygame.image.load("green.png")
    yellow = pygame.image.load("yellow.png")
    gray = pygame.image.load("gray.png")
    border = pygame.image.load("border.png")

    f = open("words.txt","r")
    words = f.readlines()

    guess = 0
    prev = []
    user_text = ''
    render_text = ''
    font = pygame.font.Font(None,60)
    state = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

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
                    prev.append(user_text)
                    guess += 1
                
                
        
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
        if len(prev) >= 1:
            for i in range(len(prev)):
                for j in range(len(prev[i])):
                    render_text += prev[i][j] + '   '
        for i in range(len(user_text)):
            render_text += user_text[i] + '   '
        surface = font.render(render_text, True, (0,0,0))
        screen.blit(surface, (33,64*guess+10))
        
        pygame.display.flip()

    f.close()

main()
