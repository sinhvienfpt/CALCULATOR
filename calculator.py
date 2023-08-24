import pygame
import webbrowser

#Init
pygame.init()

#Screen
screen = pygame.display.set_mode((500, 500))

#Colors
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORVZ = (224, 224, 224)
RES = (51, 102, 255)

#Text
usergreet = pygame.font.SysFont("Arial", 20).render("CALCULATOR                                                  by vz" \
                                                    , True, COLORVZ)

text_num_7 = pygame.font.SysFont("Arial", 20).render("7", True, BLACK)
text_num_4 = pygame.font.SysFont("Arial", 20).render("4", True, BLACK)
text_num_1 = pygame.font.SysFont("Arial", 20).render("1", True, BLACK)
text_num_0 = pygame.font.SysFont("Arial", 20).render("0", True, BLACK)
text_num_2 = pygame.font.SysFont("Arial", 20).render("2", True, BLACK)
text_num_3 = pygame.font.SysFont("Arial", 20).render("3", True, BLACK)
text_num_5 = pygame.font.SysFont("Arial", 20).render("5", True, BLACK)
text_num_6 = pygame.font.SysFont("Arial", 20).render("6", True, BLACK)
text_num_8 = pygame.font.SysFont("Arial", 20).render("8", True, BLACK)
text_num_9 = pygame.font.SysFont("Arial", 20).render("9", True, BLACK)
text_num_00 = pygame.font.SysFont("Arial", 20).render("00", True, BLACK)

text_char_point = pygame.font.SysFont("Arial", 30).render(".", True, BLACK)
text_char_divide = pygame.font.SysFont("Arial", 20).render("/", True, BLACK)
text_char_multiple = pygame.font.SysFont("Arial", 20).render("*", True, BLACK)
text_char_minus = pygame.font.SysFont("Arial", 20).render("-", True, BLACK)
text_char_plus = pygame.font.SysFont("Arial", 20).render("+", True, BLACK)
text_char_AllClear = pygame.font.SysFont("Arial", 20).render("AC", True, BLACK)
text_char_open_brackets = pygame.font.SysFont("Arial", 20).render("(", True, BLACK)
text_char_close_brackets = pygame.font.SysFont("Arial", 20).render(")", True, BLACK)
text_char_equal = pygame.font.SysFont("Arial", 20).render("=", True, BLACK)

running = True
temp = ""
while running:

    #Screen color
    screen.fill(GRAY)

    #Mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(mouse_x,mouse_y)

    #Draw
    pygame.draw.rect(screen, WHITE, (50, 25, 400, 75))
    for i in range(5):
        for j in range(4):
            pygame.draw.rect(screen, WHITE, (50 + 85 * i, 140 + 90 * j, 60, 60))

            #  -----------------
            #  |                |
            #   ----------------
            #  7   8   9  /   AC
            #  4   5   6  *   (
            #  1   2   3  -   )
            #  0   00  .  +   =

    screen.blit(usergreet, (50, 110))
    screen.blit(text_num_7, (80, 170))
    screen.blit(text_num_4, (80, 260))
    screen.blit(text_num_1, (80, 350))
    screen.blit(text_num_0, (80, 440))

    screen.blit(text_num_8, (160, 170))
    screen.blit(text_num_5, (160, 260))
    screen.blit(text_num_2, (160, 350))
    screen.blit(text_num_00, (160, 440))

    screen.blit(text_num_9, (240, 170))
    screen.blit(text_num_6, (240, 260))
    screen.blit(text_num_3, (240, 350))
    screen.blit(text_char_point, (245, 430))

    screen.blit(text_char_divide, (320, 170))
    screen.blit(text_char_multiple, (320, 260))
    screen.blit(text_char_minus, (320, 350))
    screen.blit(text_char_plus, (320, 440))

    screen.blit(text_char_AllClear, (400, 170))
    screen.blit(text_char_open_brackets, (400, 260))
    screen.blit(text_char_close_brackets, (400, 350))
    screen.blit(text_char_equal, (400, 440))

    #Event

    
    
    

    for event in pygame.event.get():
        # Quit
        if event.type == pygame.QUIT:
            running = False
        #Mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Left click
            if event.button == 1:
                if mouse_x >= 410 and mouse_x <= 447 and mouse_y >= 115 and mouse_y <= 130:
                    webbrowser.open("https://github.com/sinhvienfpt")
                if mouse_x >= 50 and mouse_x <= 110 :
                    if mouse_y>=140 and mouse_y<=200:
                        temp += "7"
                    if mouse_y>=230 and mouse_y<=290:
                        temp += "4"
                    if mouse_y>=320 and mouse_y<=380:
                        temp += "1"
                    if mouse_y>=410 and mouse_y<=470:
                        temp += "0"
                if mouse_x >= 135 and mouse_x <= 195 :
                    if mouse_y>=140 and mouse_y<=200:
                        temp += "8"
                    if mouse_y>=230 and mouse_y<=290:
                        temp += "5"
                    if mouse_y>=320 and mouse_y<=380:
                        temp += "2"
                    if mouse_y>=410 and mouse_y<=470:
                        temp += "00"
                if mouse_x >= 220 and mouse_x <= 280 :
                    if mouse_y>=140 and mouse_y<=200:
                        temp += "9"
                    if mouse_y>=230 and mouse_y<=290:
                        temp += "6"
                    if mouse_y>=320 and mouse_y<=380:
                        temp += "3"
                    if mouse_y>=410 and mouse_y<=470:
                        temp += "."
                if mouse_x >= 305 and mouse_x <= 365 :
                    if mouse_y>=140 and mouse_y<=200:
                        temp += "/"
                    if mouse_y>=230 and mouse_y<=290:
                        temp += "*"
                    if mouse_y>=320 and mouse_y<=380:
                        temp += "-"
                    if mouse_y>=410 and mouse_y<=470:
                        temp += "+"
                if mouse_x >= 390 and mouse_x <= 450 :
                    if mouse_y>=140 and mouse_y<=200:
                        temp = ""
                    if mouse_y>=230 and mouse_y<=290:
                        temp += "("
                    if mouse_y>=320 and mouse_y<=380:
                        temp += ")"
                    if mouse_y>=410 and mouse_y<=470:
                        try:
                            temp = str(eval(temp))
                        except ZeroDivisionError:
                            temp = "Zero Division Error"
    text_res = pygame.font.SysFont("Arial", 20).render(temp, True, RES)
    screen.blit(text_res, (75, 60))
    text = ""

                

    # FLip to change all color

    pygame.display.flip()

#Quit
pygame.quit()
