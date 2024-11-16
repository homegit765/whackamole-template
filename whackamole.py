import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        current_pos = (0,0)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (current_pos[0] <= event.pos[0] <= current_pos[0] + 32 and
                            current_pos[1] <= event.pos[1] <= current_pos[1] + 32):
                        current_pos = (random.randrange(0,20)*32, random.randrange(0,16)*32)
            screen.fill("light green")
            for i in range (20):
                pygame.draw.line(screen, "dark green", ((i*32)+32, 0), ((i*32)+32, 512))
            for i in range (16):
                pygame.draw.line(screen, "dark green", (0, (i*32)+32), (640, (i*32)+32))
            screen.blit(mole_image, mole_image.get_rect(topleft=current_pos))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
