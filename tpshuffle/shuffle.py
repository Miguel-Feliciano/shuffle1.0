import pygame
import pygame.freetype
import random
import time
import copy


game_grid = []
click_grid = []
score = 0
selector = 1
select1 = None
select2 = None
check = False
missed = 0
end = False

def main():
    global game_grid, click_grid, selector,select1, select2, check, score, end
    pygame.init()
    pygame.font.init()
    res = (1000, 900)
    
    screen = pygame.display.set_mode(res)
    my_font = pygame.freetype.Font("NotoSans-Regular.ttf")
    image = pygame.image.load("shuffle.png")
    
    runmenu = True
    rungame = False
   
    columns = 0
    rows = 0
    
    red = (255,0,0)
    pink =(255,200,200)
    green = (0,255,0)
    yellow = (255,255,0)
    purple = (128,0,128)
    orange = (255,165,0)
    black = (0,0,0)
    white = (255,255,255)
    darkGreen = (0,128,0)
    darkBlue = (0,0,20)

    class Text():
        def draw(self, win, text, textsize, textcolor, x, y):
            self.text = text
            self.textsize = textsize
            self.textcolor = textcolor
            self.x = x
            self.y = y
            font = pygame.font.SysFont("NotoSans-Regular.ttf", self.textsize)
            text = font.render(self.text, 1, self.textcolor)
            win.blit(text, (self.x, self.y))
    
    class Button():
        def __init__(self, color, x, y, width, height, text, textcolor, textsize):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text
            self.textcolor = textcolor
            self.textsize = textsize
        
        def draw(self, win):
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 2)
            
            if self.text != None:
                font = pygame.font.SysFont("NotoSans-Regular.ttf", self.textsize)
                text = font.render(self.text, 1, self.textcolor)
                win.blit(text, (self.x + (int(self.width/2) - int(text.get_width()/2)), self.y + (int(self.height/2) - int(text.get_height()/2))))
    
    class Card():
        def __init__(self, color, shape, shape_color):
            self.color = color
            self.shape = shape
            self.shape_color = shape_color
        
        def draw(self, win, x , y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)
            if self.shape == "square":
                self.shape_width = int(self.width/2)
                self.shape_height = int(self.width/2)
                self.shape_x = self.x + int(self.shape_width/2)
                self.shape_y = self.y + int(self.height/2 - int(self.shape_height/2))
                pygame.draw.rect(win, self.shape_color, (self.shape_x, self.shape_y, self.shape_width, self.shape_height))
            elif self.shape == "circle":
                self.shape_x = self.x + int(self.width/2)
                self.shape_y = self.y + int(self.height/2)
                pygame.draw.circle(win, self.shape_color, (self.shape_x, self.shape_y), int(self.width/4))
            elif self.shape == "triangle":
                pygame.draw.polygon(win , self.shape_color , [(self.x + int(self.width/2), (self.y + int(self.height/2)) - int(self.height/4))  , (self.x + int(self.width/4), self.y + int(self.height/2) + int(self.width/4)) , (self.x + self.width - int(self.width/4), self.y + int(self.height/2) + int(self.width/4))])
    
    scoretext = Text()

    Blevel1 = Button(yellow, res[0]/2 - 75, res[1]/2, 150, 50, "Level1", yellow, 40)
    Blevel2 = Button(yellow, res[0]/2 - 75, res[1]/2 +60, 150, 50, "Level2", yellow, 40)
    Blevel3 = Button(yellow, res[0]/2 - 75, res[1]/2 + 120, 150, 50, "Level3", yellow, 40)
    Blevel4 = Button(yellow, res[0]/2 - 75, res[1]/2 + 180, 150, 50, "Level4", yellow, 40)
    Blevel5 = Button(yellow, res[0]/2 - 75, res[1]/2 + 240, 150, 50, "Level5", yellow, 40)
    Blevel6 = Button(yellow, res[0]/2 - 75, res[1]/2 + 300, 150, 50, "Level6", yellow, 40)
    Bexitmenu = Button(yellow, res[0]/2 - 75, res[1]/2 + 360, 150, 50, "Exit", yellow, 40)
    Bexitgame = Button(yellow, 10, res[1] - 60, 150, 50, "Exit", yellow, 40)
    Bquit = Button(yellow, 10, res[1] - 60, 150, 50, "Quit", yellow, 40)
            
           
    c1 = Card(darkBlue, "square", red)
    c2 = Card(darkBlue, "square", pink)
    c3 = Card(darkBlue, "square", yellow)
    c4 = Card(darkBlue, "square", purple)
    c5 = Card(darkBlue, "square", orange)
    c6 = Card(darkBlue, "square", darkGreen)
    c7 = Card(darkBlue, "circle", red)
    c8 = Card(darkBlue, "circle", pink)
    c9 = Card(darkBlue, "circle", yellow)
    c10 = Card(darkBlue, "circle", purple)
    c11 = Card(darkBlue, "circle", orange)
    c12 = Card(darkBlue, "circle", darkGreen)
    c13 = Card(darkBlue, "triangle", red)
    c14 = Card(darkBlue, "triangle", pink)
    c15 = Card(darkBlue, "triangle", yellow)
    c16 = Card(darkBlue, "triangle", purple)
    c17 = Card(darkBlue, "triangle", orange)
    c18 = Card(darkBlue, "triangle", darkGreen)
        
    def game_gen():
        global game_grid, click_grid
        game_grid = []
        click_grid = []
        game_cards = []
        cards = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, c17, c18]
        random.shuffle(cards)
        for x in range(int(rows*columns/2)):
            game_cards.append(cards.pop())
            game_cards.append(copy.deepcopy(game_cards[-1]))
        random.shuffle(game_cards)
        for x in range(rows):
            aux_list = []
            click_grid.append([])
            for y in range(columns):
                aux_list.append(game_cards.pop())
                click_grid[x].append(0)
            game_grid.append(aux_list)
    
    def match_check():
        global select1, select2, check, score, end
        if game_grid[select1[0]][select1[1]] != None and game_grid[select2[0]][select2[1]] != None:
            if select1 != select2:
                if game_grid[select1[0]][select1[1]].shape == game_grid[select2[0]][select2[1]].shape:
                    if game_grid[select1[0]][select1[1]].shape_color == game_grid[select2[0]][select2[1]].shape_color:
                        game_grid[select1[0]][select1[1]] = None
                        game_grid[select2[0]][select2[1]] = None
                        score += 100
                        check = False
                    else:
                        mismatched()
                else:
                    mismatched()
            else:
                mismatched()
        else:
            mismatched()
        if score < 0:
            score = 0
        end = True
        for x in range(rows):
            for y in range(columns):
                if click_grid[x][y] == 0:
                    end = False
        
        pygame.display.flip()                        
        time.sleep(1)
        
        
    def mismatched():
        global chick_grid, select1,select2, score, missed, check
        click_grid[select1[0]][select1[1]] = 0
        click_grid[select2[0]][select2[1]] = 0
        score -= missed * 20
        missed += 1
        check = False
        
    while runmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runmenu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    runmenu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if Blevel1.x < pos[0] < (Blevel1.x + Blevel1.width):
                    if Blevel1.y < pos[1] < (Blevel1.y + Blevel1.height):
                        rows = 3
                        columns = 4
                        game_gen()
                        rungame = True
                        
                if Blevel2.x < pos[0] < (Blevel2.x + Blevel2.width):
                    if Blevel2.y < pos[1] < (Blevel2.y + Blevel2.height):
                        rows = 4
                        columns = 4
                        game_gen()
                        rungame = True
                        
                if Blevel3.x < pos[0] < (Blevel3.x + Blevel3.width):
                    if Blevel3.y < pos[1] < (Blevel3.y + Blevel3.height):
                        rows = 4
                        columns = 5
                        game_gen()
                        rungame = True
    
                if Blevel4.x < pos[0] < (Blevel4.x + Blevel4.width):
                    if Blevel4.y < pos[1] < (Blevel4.y + Blevel4.height):
                        rows = 4
                        columns = 6
                        game_gen()
                        rungame = True

                if Blevel5.x < pos[0] < (Blevel5.x + Blevel5.width):
                    if Blevel5.y < pos[1] < (Blevel5.y + Blevel5.height):
                        rows = 5
                        columns = 6
                        game_gen()
                        rungame = True

                if Blevel6.x < pos[0] < (Blevel6.x + Blevel6.width):
                    if Blevel6.y < pos[1] < (Blevel6.y + Blevel6.height):
                        rows = 6
                        columns = 6
                        game_gen()
                        rungame = True
                
                if Bexitmenu.x < pos[0] < (Bexitmenu.x + Bexitmenu.width):
                    if Bexitmenu.y < pos[1] < (Bexitmenu.y + Bexitmenu.height):
                        runmenu = False
                        
        screen.fill(darkBlue)
        mbuttons = (Blevel1, Blevel2, Blevel3, Blevel4, Blevel5, Blevel6, Bexitmenu)
        for button in mbuttons:
            button.draw(screen)
        
        screen.blit(image, (120, 50))  
        
        pygame.display.flip()
        
          
        while rungame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rungame = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        rungame = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if Bexitgame.x < pos[0] < (Bexitgame.x + Bexitgame.width):
                        if Bexitgame.y < pos[1] < (Bexitgame.y + Bexitgame.height):
                            score = 0
                            rungame = False
                    for i in range(rows):
                        for j in range(columns):
                            if game_grid[i][j] == None:
                                continue
                            else:
                                if game_grid[i][j].x < pos[0] < game_grid[i][j].x + game_grid[i][j].width:
                                    if game_grid[i][j].y < pos[1] < game_grid[i][j].y + game_grid[i][j].height:
                                        click_grid[i][j] = 1
                                        if selector == 1:
                                            select1 = (i, j)
                                            selector = 2
                                        elif selector == 2:
                                            select2 = (i, j)
                                            selector = 1
                                            check = True
                                        else:
                                            continue
            screen.fill(darkBlue)
            Bexitgame.draw(screen)
            scoretext.draw(screen, "Congratulation! Score: {}".format(score), 20, white, 10, 10)
            
            for x in range(rows):
                for y in range(columns):
                    if game_grid[x][y] == None:
                       continue
                    else:
                        game_grid[x][y].draw(screen, 190 + int(600/columns) * y + 30 * y, int(120/(rows+1)) + int(600/rows) * x + int(120/(rows+1)) * x, int(600/columns), int(600/rows))
                    if click_grid[x][y] == 0:
                        pygame.draw.rect(screen, green, (game_grid[x][y].x, game_grid[x][y].y, game_grid[x][y].width, game_grid[x][y].height), 0)
                        
            if check:
                match_check()      

            pygame.display.flip()
            
            while end:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        end = False
                        rungame = False
                        score = 0
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            end = False
                            rungame = False
                            score = 0 
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if Bquit.x < pos[0] < (Bexitgame.x + Bexitgame.width):
                            if  Bexitgame.y < pos[1] < (Bexitgame.y +Bexitgame.height): 
                                end = False
                                rungame = False
                                score = 0
                
                screen.fill(darkBlue)
                scoretext.draw(screen, "Congratulations! Score: {}".format(score), 45, green, 310, 400)
                Bquit.draw(screen)
                pygame.display.flip()
        
main()