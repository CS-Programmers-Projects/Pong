import pygame
from pygame.locals import *
from GameManager import *
fps_clock = pygame.time.Clock()
fps = 40 # Number of frames per second

# Main function
def main():
    pygame.init()

    # game = GameManager()

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            # mouse movement commands
            elif event.type == MOUSEMOTION:
                pass
                #game.move_player(event.pos)

        # game.update()
        pygame.display.update()
        fps_clock.tick(fps)


if __name__ == '__main__':
    main()