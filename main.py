import pygame
from components import *

# Ініціалізація Pygame
pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 20)  

# Розміри вікна
width = 1280
height = 720

# Ініціалізація вікна
window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("РГПУ-2100")
clock = pygame.time.Clock()

# Фон та кольори
blue = (0, 255, 255)
brown = (153, 51, 0)
green = (124, 252, 0)
dark_green = (34,139,34)
purple = (138,43,226)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
gravity = 1
class Label(Area):
    def set_text(self, text, font_size=18, text_color=(0, 0, 0)):
        self.text = text
        self.image = pygame.font.SysFont('verdana', font_size).render(text, True, text_color)

    def draw(self, window, shift_x=0, shift_y=0):
        window.blit(self.image, (self.rect.x, self.rect.y - camera_y, self.rect.width, self.rect.height))

# об'єкти для початкового меню
menu_start_button = Picture("graphics/menu_start_button.png", 550, 300, width=160, height=160)
darken_start_button = Picture("graphics/dark_menu_start_button.png", 550, 300, width=160, height=160)
menu_settings_button = Picture("graphics/menu_settings.png", 425, 450, width=110, height=110)
darken_settings_button = Picture("graphics/dark_menu_settings.png", 425, 450, width=110, height=110)
menu_credits_button = Picture("graphics/menu_credits.png", 575, 550, width=110, height=110)
darken_credits_button = Picture("graphics/dark_menu_credits.png", 575, 550, width=110, height=110)
menu_exit_button = Picture("graphics/exit_button.png", 725, 450, width=110, height=110)
darken_exit_button = Picture("graphics/dark_exit_button.png", 725, 450, width=110,height=110)

#об'єкти для налаштувань
how_to_play = Label(25,125,100,50)
how_to_play.set_text("Донесіть прапор до фінішу, натискаючи на клавіші, які будуть появлятись на екрані, для того щоб стрибати по платформах")
something_to_dramatize = Label(25,200,100,50)
something_to_dramatize.set_text("Прапор потрібен зверху. Донесіть туди його, де він потрібен.")

#Автори
game_designers = Label(25,125,100,50)
game_designers.set_text("Гейм дизайнер: Юник Вадим")
programmers = Label(25,200,100,50)
programmers.set_text("Програмісти: Юник Вадим, ChatGPT, Bing AI, Данило Матюк")
game_artists = Label(25, 275, 100, 50)
game_artists.set_text("Художники: Юник Вадим, DALL-E")
testers = Label(25, 350, 100, 50)
testers.set_text("Тестери: Юник Вадим, Данило Матюк")

#об'єкти для гри
finish = Label(100, width // 6, 100,50)
finish.set_text("Дякую, ти приніс прапор. Тепер повернись на позиції, але обережно, земля замінована!")

# універсальні об'єкти
back_button = Picture("graphics/back_button.png", 40, 30, width=95, height=75)
darken_back_button = Picture("graphics/dark_back_button.png", 40, 30, width=95, height=75)

# Клас для головного персонажа
player_image = pygame.image.load("graphics/player.png")
player_image = pygame.transform.scale(player_image, (50, 50))
key_left = pygame.K_LEFT
key_right = pygame.K_RIGHT
key_jump = pygame.K_SPACE

class Player:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.y_velocity = 0
        self.speed = speed
        self.jump_power = 15

    def update(self):

        keys = pygame.key.get_pressed()
        if keys[key_left]:
            self.rect.x -= self.speed
        if keys[key_right]:
            self.rect.x += self.speed
        if keys[key_jump]:
            self.rect.y -= self.jump_power
   
        self.y_velocity += gravity
        self.rect.y += self.y_velocity

    def draw(self):
        window.blit(player_image, (self.rect.x, self.rect.y - camera_y))


class Platform:
    def __init__(self, x, y, width, height, speed, direction, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.direction = direction
        self.color = color

    def move(self):
        self.rect.x += self.speed * self.direction

        if self.rect.right >= width or self.rect.left <= 0:
            self.direction *= -1

    def draw(self):
        pygame.draw.rect(window, self.color, (self.rect.x, self.rect.y - camera_y, self.rect.width, self.rect.height))

camera_speed = 5
camera_limit = height // 4
camera_y = 0
player = Player(width // 2 - 25, height -60, 50, 50, 5)
#x, y, width, height, speed, direction, color
platform1 = Platform(400, height - 200, 70, 20, 3, -1, brown)
platform2 = Platform(200, height - 300, 70, 20, 4, 1, brown)
platform3 = Platform(0, height - 400,70, 20, 0, 1, brown)
platform4 = Platform(100,height - 500,70, 20, 5, 1, brown)
platform5 = Platform(700,height - 600,70, 20, 0, 1, brown)
platform6 = Platform(860,height - 700,70, 20, 0, 1, brown)
platform7 = Platform(150,height - 800,70, 20, 5, 1, brown)
platform8 = Platform(0,-180, 620, 20, 0, 1, dark_green)
platform8_9= Platform(width // 2, -320, 70, 20, 3,-1, dark_green) 
platform9 = Platform(-350,-450,500, 20, 0, 1, dark_green)
platform10 = Platform(800, -580, 100, 20, 3, -1, brown)
platform11 = Platform(0, -750, 20, 20, 3, 1, dark_green)
platform12 = Platform(640, -850, 20, 20, 3, -1, dark_green)
platform13 = Platform(100, -950, 20, 20, 3, 1, dark_green)
platform14 = Platform(100, -1050, 70, 20, 0, 1, purple)
platform15 = Platform(100, -1150, 70, 20, 0, 1, purple)
platform16 = Platform(100, -1250, 70, 20, 0, 1, purple)
platform17 = Platform(100, -1350, 70, 20, 0, 1, purple)
platform18 = Platform(100, -1450, 70, 20, 0, 1, purple)
platform14_2 = Platform(1110, -1050, 70, 20, 0, 1, purple)
platform15_2 = Platform(1110, -1150, 70, 20, 0, 1, purple)
platform16_2 = Platform(1110, -1250, 70, 20, 0, 1, purple)
platform17_2 = Platform(1110, -1350, 70, 20, 0, 1, purple)
platform18_2 = Platform(1110, -1450, 70, 20, 0, 1, purple)
platform19 = Platform(500, -1600, 70, 20, 6, 1, dark_green)
platform20 = Platform(0, -1650, 90, 20, 4, 1, dark_green)
platform21 = Platform(0, -1750, 50, 20, 2, 1, dark_green)
platform22 = Platform(0, -1850, 60, 20, 3, 1, dark_green)
platform23 = Platform(0, -1950, 150, 20, 5, 1, dark_green)
platform24 = Platform(0, -2050, 20, 20, 1, 1, dark_green)
platform25 = Platform(0, -2150, 50, 20, 2, 1, dark_green)
platform26 = Platform(0, -2250, 70, 20, 4, 1, dark_green)
platform27 = Platform(0, -2350, 30, 20, 3, 1, dark_green)
platform28 = Platform(0, -2450, 100, 20, 4, 1, dark_green)
platform29 = Platform(0, -2550, 90, 20, 2, 1, dark_green)
platform30 = Platform(width - 200, -2650, 100, 15, 0, 1, yellow)
platform31 = Platform(width - 350, -2800, 100, 15, 0, 1, yellow)
platform32 = Platform(width - 500, -2950, 100, 15, 0, 1, yellow)
platform33 = Platform(width - 650, -3100, 100, 15, 0, 1, yellow)
platform34 = Platform(width - 800, -3250, 100, 15, 0, 1, yellow)
platform35 = Platform(width - 950, -3400,  100, 15, 0, 1, yellow)
platform36 = Platform(width - 1100, -3550,  100, 15, 0, 1, yellow)
platform37 = Platform(50, -3700,  100, 15, 0, 1, yellow)
platform38 = Platform(200, -3850,  100, 15, 0, 1, yellow)
platform39 = Platform(350, -4000,  100, 15, 0, 1, yellow)
platform40 = Platform(500, -4150,  100, 15, 0, 1, yellow)
platform41 = Platform(650, -4300,  100, 15, 0, 1, yellow)
platform42 = Platform(800, -4450,  100, 15, 0, 1, yellow)
platform43 = Platform(950, -4600,  100, 15, 0, 1, yellow)
platform44 = Platform(1100, -4750,  100, 15, 0, 1, yellow)
platform45 = Platform(0, -4900,  width - 250, 20, 0, 1, dark_green)
platform46 = Platform(0, -5050, 200, 17, 0, 1, dark_green)
platform46_47 = Platform(0, -5200,80, 17, 5, 1, dark_green)
platform47 = Platform(480, -5300, 800, 17, 0, 1, dark_green)
platform48 = Platform(width // 2, -5450, 20,20, 0, 1, purple)
platform49 = Platform(width // 2, -5600, 20,20, 0, 1, purple)
platform50 = Platform(width // 2, -5750, 20,20, 0, 1, purple)
platform51 = Platform(width // 2, -5900, 20,20, 0, 1, purple)
platform52 = Platform(width // 2, -6050, 20,20, 0, 1, purple)
platform53 = Platform(width // 2, -6200, 20,20, 0, 1, purple)
platform54 = Platform(width // 2, -6350, 20,20, 0, 1, purple)
platform55 = Platform(width // 2, -6500, 20,20, 0, 1, purple)
platform56 = Platform(width // 2, -6650, 20,20, 0, 1, purple)
platform57 = Platform(width // 2, -6800, 20,20, 0, 1, purple)
platform58 = Platform(width // 2, -6950, 20,20, 0, 1, purple)
platform59 = Platform(0, -7100, 70, 15, 5, 1, brown)
platform60 = Platform(500, -7250, 70, 15, 5, -1, brown)
platform61 = Platform(0, -7400, 70, 15, 5, 1, brown)
base_platform = Platform(0, height - 40, width, 200, 0, 0, green)

finish_platform = Platform(0, -7550, width- 100, 30, 0, 0, green)
platforms = [base_platform,platform1, platform2, platform3, platform4,platform5, platform6, platform7, platform8,platform9,platform8_9,platform10,platform11,platform12,platform13,platform14,platform15,platform16,platform17,platform18,platform14_2,platform15_2,platform16_2,platform17_2,platform18_2,platform19,platform20,platform21,platform22,platform23,platform24,platform25,platform26,platform27,platform28,platform29,platform30,
platform31, platform32,platform33, platform34, platform35, platform36, platform37, platform38, platform39, platform40, platform41,platform42, platform43,platform44, platform45, platform46, platform46_47, platform47, platform48, platform49, platform50, platform51,platform52,platform53,platform54,platform55,platform56, platform57, platform58, platform59, platform60, platform61, finish_platform]


# Головний цикл гри
running = True
full_screen = False
screen = "menu"
key_changing = False

while running:
    window.fill(blue)

    if screen == "menu":
        for event in pygame.event.get():
            # вихід
            if event.type == pygame.QUIT:
                running = False

            # зміна форми вікна
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    full_screen = not full_screen
                    if full_screen:
                        window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    else:
                        window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if menu_settings_button.rect.collidepoint(x, y):
                    screen = "settings"
                elif menu_credits_button.rect.collidepoint(x, y):
                    screen = "credits"
                elif menu_start_button.rect.collidepoint(x, y):
                    screen = "game"
                elif menu_exit_button.rect.collidepoint(x,y):
                    running = False
                

        # Кнопка старту
        mouse_pos = pygame.mouse.get_pos()
        if menu_start_button.rect.collidepoint(mouse_pos):
            darken_start_button.draw(window)
        else:
            menu_start_button.draw(window)

        # Кнопка налаштування
        if menu_settings_button.rect.collidepoint(mouse_pos):
            darken_settings_button.draw(window)
        else:
            menu_settings_button.draw(window)

        # Кнопка credits
        if menu_credits_button.rect.collidepoint(mouse_pos):
            darken_credits_button.draw(window)
        else:
            menu_credits_button.draw(window)
        
        #кнопка виходу з гри
        if menu_exit_button.rect.collidepoint(mouse_pos):
            darken_exit_button.draw(window)
        else:
            menu_exit_button.draw(window)

    elif screen == "settings":
        for event in pygame.event.get():
            # вихід
            if event.type == pygame.QUIT:
                running = False

            # зміна форми вікна
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    full_screen = not full_screen
                    if full_screen:
                        window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    else:
                        window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if back_button.rect.collidepoint(x, y):
                    screen = "menu"

        # Вихід
        mouse_pos = pygame.mouse.get_pos()
        if back_button.rect.collidepoint(mouse_pos):
            darken_back_button.draw(window)
        else:
            back_button.draw(window)
        
        how_to_play.draw(window)
        something_to_dramatize.draw(window)

    elif screen == "credits":
        for event in pygame.event.get():
            # вихід
            if event.type == pygame.QUIT:
                running = False

            # зміна форми вікна
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    full_screen = not full_screen
                    if full_screen:
                        window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    else:
                        window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if back_button.rect.collidepoint(x, y):
                    screen = "menu"

        # Вихід
        mouse_pos = pygame.mouse.get_pos()
        if back_button.rect.collidepoint(mouse_pos):
            darken_back_button.draw(window)
        else:
            back_button.draw(window)
        # Автори
        game_designers.draw(window)
        programmers.draw(window)
        game_artists.draw(window)
        testers.draw(window)


    elif screen == "game":
        for event in pygame.event.get():
            # вихід
            if event.type == pygame.QUIT:
                running = False

            # зміна форми вікна
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    full_screen = not full_screen
                    if full_screen:
                        window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                    else:
                        window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            
                #чіти
                if event.key == pygame.K_q:
                    gravity = 0
                if event.key == pygame.K_w:
                    gravity = 1
                        
        player.update()
        if player.rect.y < camera_limit:
            camera_y = player.rect.y - camera_limit
        elif player.rect.y + player.rect.height > height - 150:
            camera_y = player.rect.y + player.rect.height - (height - 150)
        else:
            camera_y = 0

        player.rect.y -= camera_y
        for platform in platforms:
            platform.rect.y -= camera_y

        for platform in platforms:
            if player.rect.colliderect(platform.rect):
                player.y_velocity = 0
                player.rect.y = platform.rect.y - player.rect.height
                if platform == finish_platform:
                    finish.draw(window)

        for platform in platforms:
            platform.move()
        
        player.draw()
        for platform in platforms:
            platform.draw()
    
        pygame.display.flip()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()