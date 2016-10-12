# pygame template by Josh Cockrell jokcua@gmail.com

import pygame
pygame.init()

def game_proceedure(event):
    """ """

    # Keyboard Messages
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            a = 1
    else:
        return

def main():

    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Template")
    background_color = pygame.Surface(screen.get_size()).convert()
    background_color.fill((240,50,0))

    clock = pygame.time.Clock()
    running = True

    while running:
        
        clock.tick(30)

        for event in pygame.event.get():

            game_proceedure(event)
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_color, (0,0))
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()
