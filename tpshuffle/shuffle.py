import pygame
import pygame.freetype
yellow = (255, 255, 0)
white = (255, 255, 255)

def main():
    
    pygame.init()
    run = True
    res = (1000, 800)
    game = True
    game_gen = False
    pos = pygame.mouse.get_pos()
    rows = 1
    columns = 1
    screen = pygame.display.set_mode(res)
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf", 24)
    image = pygame.image.load("shuffle.png")
    screen.fill((0,0,20))

    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()
                print(click)
                if 450 < pos[0] < 550:
                    if 300 < pos[1] < 335:  
                        rows = 3
                        columns = 4
                        game_gen()
                        rungame = True
                        
                if 450 < pos[0] < 550:
                    if 350 < pos[1] < 385:
                        rows = 4
                        columns = 4
                        game_gen()
                        rungame = True
                        
                if 450 < pos[0] < 550:
                    if 400 < pos[1] < 435:
                        rows = 5
                        columns = 4
                        game_gen()
                        rungame = True
    
                if 450 < pos[0] < 550:
                    if 450 < pos[1] < 485:
                        rows = 6
                        columns = 4
                        game_gen()
                        rungame = True

                if 450 < pos[0] < 550:
                    if 500 < pos[1] < 535:
                        rows = 6
                        columns = 5
                        game_gen()
                        rungame = True

                if 450 < pos[0] < 550:
                    if 550 < pos[1] < 585:
                        rows = 6
                        columns = 6
                        game_gen()
                        rungame = True
                
                if 25 < pos[0] < 125:
                    if 750 < pos[1] < 785:
                        run = False
        
            
        mouse = pygame.mouse.get_pos()   
           
        if 450 +100 > mouse[0] > 450 and 300 + 35 > mouse[1] > 300:
            pygame.draw.rect(screen, white, (450, 300, 100, 35), 3)
        else:
            pygame.draw.rect(screen, yellow, (450, 300, 100, 35), 3)
                
        if 450 +100 > mouse[0] > 450 and 350 + 35 > mouse[1] > 350:     
            pygame.draw.rect(screen, white, (450, 350, 100, 35), 3)
        else:
            pygame.draw.rect(screen, yellow, (450, 350, 100, 35), 3)
                
        if 450 +100 > mouse[0] > 450 and 450 + 35 > mouse[1] > 400:
            pygame.draw.rect(screen, white, (450, 400, 100, 35), 3)
        else:
            pygame.draw.rect(screen, yellow, (450, 400, 100, 35), 3)
        
        if 450 +100 > mouse[0] > 450 and 500 + 35 > mouse[1] > 450:
            pygame.draw.rect(screen, white, (450, 450, 100, 35), 3)
        else:
            pygame.draw.rect(screen, yellow, (450, 450, 100, 35), 3)
            
        if 450 +100 > mouse[0] > 450 and 550 + 35 > mouse[1] > 500:
            pygame.draw.rect(screen, white, (450, 500, 100, 35), 3)
        else:
            pygame.draw.rect(screen, yellow, (450, 500, 100, 35), 3)
        
        if 450 +100 > mouse[0] > 450 and 550 + 35 > mouse[1] > 550:
            pygame.draw.rect(screen, white, (450, 550, 100, 35), 3)
        else:
            pygame.draw.rect(screen, yellow, (450, 550, 100, 35), 3)
        
        if 25 +100 > mouse[0] > 25 and 750 + 35 > mouse[1] > 750:
            pygame.draw.rect(screen, white, (25, 750, 100, 35), 3)
        else:
            pygame.draw.rect(screen, yellow, (25, 750, 100, 35), 3)
            
            
            
            my_font.render_to(screen, (465, 310), "Level 1", yellow)
            my_font.render_to(screen, (465, 360), "Level 2", yellow)
            my_font.render_to(screen, (465, 410), "Level 3", yellow)
            my_font.render_to(screen, (465, 460), "Level 4", yellow)
            my_font.render_to(screen, (465, 510), "Level 5", yellow)
            my_font.render_to(screen, (465, 560), "Level 6", yellow)
            my_font.render_to(screen, (50, 760), "QUIT", yellow)
            
        screen.blit(image, (50, 50))
        pygame.display.flip()
        '''
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 25 < pos[0] and (25 + 100) > pos[0]:
                        if 750 < pos[1] and (750 + 35) > pos[1]:
                            score = 0
                            game = False
                    for i in range(rows):
                        for j in range(columns):
                            if game_grid[1][j] == None:
                                continue
                            else:
                                if game_grid[i][j].x < pos[0] and game_grid[i][j].y < pos[1]:
                                    if game_grid[i][j].x + game_grid[i][j].width > pos[0] and game_grid[i][j].y + game_grid[i][j].height > pos[1]:
                                        click_grid[i][j] = 1
                                        if select == 1:
                                            select1 = (i, j)
                                            select = 2
                                        elif select == 2:
                                            select2 = (i, j)
                                            select = 1
                                            check = True
                                        '''
                     
        
        
    
main()