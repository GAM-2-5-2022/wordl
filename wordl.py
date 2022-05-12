import pygame

def main():
    pygame.init()

    logo = pygame.image.load("wordl32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("wordl")

    screen = pygame.display.set_mode((400,550))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
main()
