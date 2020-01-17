import pygame
import pygame.freetype

def main():
    pygame.init()
    res = (700, 660)
    screen = pygame.display.set_mode(res)
    while(True):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                exit()

        
        screen.fill((0, 0, 50))
        rect1 = pygame.draw.rect(screen, (123, 0, 100), (320, 200, 150, 40), 0)
        rect2 = pygame.draw.rect(screen, (123, 0, 100), (320, 270, 150, 40), 0)
        rect3 = pygame.draw.rect(screen, (123, 0, 100), (320, 340, 150, 40), 0)
        rect4 = pygame.draw.rect(screen, (123, 0, 100), (320, 410, 150, 40), 0)
        rect5 = pygame.draw.rect(screen, (123, 0, 100), (320, 490, 150, 40), 0)
        rect6 = pygame.draw.rect(screen, (123, 0, 100), (320, 550, 150, 40), 0)



        image = pygame.image.load("shuffle.png")
        screen.blit(image, (0, 0))


        my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
        font1 = my_font.render_to(screen, (350, 210), "3 x 4", (255, 255, 0))
        font2 = my_font.render_to(screen, (350, 280), "4 x 4", (255, 255, 0))
        font3 = my_font.render_to(screen, (350, 350), "5 x 4", (255, 255, 0))
        font4 = my_font.render_to(screen, (350, 420), "6 x 4", (255, 255, 0))
        font5 = my_font.render_to(screen, (350, 490), "6 x 5", (255, 255, 0))
        font6 = my_font.render_to(screen, (350, 560), "6 x 6", (255, 255, 0))

        pygame.display.flip()

main()

