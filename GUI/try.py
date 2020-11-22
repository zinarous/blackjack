import pygame
pygame.init()
WIDTH = 1600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()
background_image = pygame.image.load('background.png')
logo_img = pygame.image.load('logo.png')

pygame.mixer.init()
pygame.mixer.music.load("background_s.mp3")
pygame.mixer.music.set_volume(0.01)

def vol_sound(name):
    fullname = "but_fat.mp3"     # path + name of the sound file
    sound = pygame.mixer.Sound(fullname)
    sound.set_volume(0.1)
    return sound
button_sound = vol_sound('but_fat.mp3')

class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (45,146,110)
        self.active_color = (56,170,130)
    def draw(self, x, y, msg, screen, action=None, font_size=19):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.active_color, (x , y , self.width, self.height))
            
            if click[0] == 1:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(300)#временная задержка, чтобы постоянно не проигрывался звук
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()
        else:
            pygame.draw.rect(screen, self.inactive_color, (x, y, self.width, self.height))

        print_text(message=msg, x=x + 7, y=y + 25, font_size=font_size)
        
def print_text(message, x, y, font_color = (255, 255, 255), font_type = "bold.ttf", font_size = 19):
    font_type = pygame.font.Font(font_type, font_size, bold=True)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))
    
# def pause():
#     pygame.mixer.music.pause()


start_button = Button(200, 80)
quit_button = Button(112, 80)
pygame.mixer.music.play(-1)#запуск фоновой музыки
def game():
    backgr = pygame.image.load('backgr.png')
    show = True
    while show:
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверка закрытия окна
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(backgr, (0, 0))
        pygame.display.update()
        clock.tick(60)

def end_game():
    backgr = pygame.image.load('backgr.png')
    restart_button = Button(200, 80)
    quit1_button = Button(112, 80)

    end = True
    while end:
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверка закрытия окна
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(backgr, (0, 0))
        restart_button.draw(700, 500, 'НАЧАТЬ ЗАНОВО', screen, main_game, 19)
        quit1_button.draw(740, 600, 'ВЫХОД', screen, quit, 19)

        pygame.display.update()
        clock.tick(60)
def main_game():
    global run_game, vol_sound, print_text
def run_game():
# Цикл игры
    running = True # флаг выхода из цикла игры
    while running:
        # Отслеживание события: "закрыть окно"
        screen.blit(background_image, (0, 0))
        screen.blit(logo_img, (500, 200))
        start_button.draw(700, 500, 'НАЧАТЬ ИГРУ', screen, game, 19)
        quit_button.draw(740, 600, 'ВЫХОД', screen, quit, 19)
        pygame.display.update()
        clock.tick(60)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверка закрытия окна
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
run_game()
