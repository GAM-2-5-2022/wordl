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

    screen = pygame.display.set_mode((350,390))

    running = True
    
    while running:
        
        screen.fill((255,255,255))
        for i in range(5):
            for j in range(6):
                screen.blit(border, (64*i + 15,64*j))
        
        pygame.display.flip()




        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
main()
