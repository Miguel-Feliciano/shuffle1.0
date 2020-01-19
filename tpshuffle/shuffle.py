import pygame
import pygame.freetype

def main():

    pygame.init()

    res = (1000, 800)
    screen = pygame.display.set_mode(res)
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
    image = pygame.image.load("shuffle.png")
    while (True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                exit()
        screen.fill((0, 0, 20))
        screen.blit(image, (50,0))
        pygame.draw.rect(screen, (255, 255, 0), (450, 400, 100, 35), 3)
        pygame.draw.rect(screen, (255, 255, 0), (450, 450, 100, 35), 3)
        pygame.draw.rect(screen, (255, 255, 0), (450, 350, 100, 35), 3)
        pygame.draw.rect(screen, (255, 255, 0), (450, 300, 100, 35), 3)
        pygame.draw.rect(screen, (255, 255, 0), (450, 500, 100, 35), 3)
        pygame.draw.rect(screen, (255, 255, 0), (450, 550, 100, 35), 3)
        pygame.draw.rect(screen, (255, 255, 0), (25, 750, 100, 35), 3)
        my_font.render_to(screen, (465, 310), "Level 1", (255, 255, 0))
        my_font.render_to(screen, (465, 360), "Level 2", (255, 255, 0))
        my_font.render_to(screen, (465, 410), "Level 3", (255, 255, 0))
        my_font.render_to(screen, (465, 460), "Level 4", (255, 255, 0))
        my_font.render_to(screen, (465, 510), "Level 5", (255, 255, 0))
        my_font.render_to(screen, (465, 560), "Level 6", (255, 255, 0))
        my_font.render_to(screen, (50, 760), "QUIT", (255, 255, 0))
        
        

        pygame.display.flip()

main()