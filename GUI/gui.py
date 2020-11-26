import pygame, sys
from main import start_g

pygame.init()
WIDTH = 1600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")
pygame.display.set_icon(pygame.image.load('icon.png'))
clock = pygame.time.Clock()
background_image = pygame.image.load('background.png')
logo_img = pygame.image.load('logo.png')

pygame.mixer.init()
pygame.mixer.music.load("background_s.mp3")
pygame.mixer.music.set_volume(0.01)

def vol_sound(name):
    fullname = "but_fat.mp3"
    sound = pygame.mixer.Sound(fullname)
    sound.set_volume(0.1)
    return sound
button_sound = vol_sound('but_fat.mp3')

#функции для кнопок музыки
def c_sound_btn_off():
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        pygame.mixer.music.pause()

def c_sound_btn_on():
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        pygame.mixer.music.unpause()
            
class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (45,146,110)
        self.active_color = (56,170,130)

    def draw(self, x, y, screen, action=None):
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

    def print_text(self, message, x, y, font_color = (255, 255, 255), font_type = "bold.ttf", font_size = 19):
        font_type = pygame.font.Font(font_type, font_size, bold=True)
        text = font_type.render(message, True, font_color)
        screen.blit(text, (x, y))
    
snd_btn_on = Button(95, 60)
snd_btn_off = Button(95, 60)
start_button = Button(200, 80)
quit_button = Button(200, 80)
sound_text = Button(0, 0)
pygame.mixer.music.play(-1)#запуск фоновой музыки

def game():
    pygame.display.iconify()
    start_g()
    if start_g() is False:
        pygame.display.get_active()
    # backgr = pygame.image.load('backgr.png')
    # show = True
    # while show:
    #     # Ввод процесса (события)
    #     for event in pygame.event.get():
    #         # проверка закрытия окна
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             quit()

    #     screen.blit(backgr, (0, 0))
    #     pygame.display.update()
    #     clock.tick(60)

# Цикл игры
def run_game():
    running = True # флаг выхода из цикла игры
    while running:
        # Отслеживание события: "закрыть окно"
        screen.blit(background_image, (0, 0))
        screen.blit(logo_img, (500, 200))
        start_button.draw(700, 500, screen, game)
        start_button.print_text('НАЧАТЬ ИГРУ', 702, 530, font_size = 20)
        quit_button.draw(700, 600, screen, quit)
        quit_button.print_text('ВЫХОД', 745, 630, font_size = 20)
        snd_btn_on.draw(90, 830, screen, c_sound_btn_on)
        snd_btn_on.print_text('ВКЛ', 110, 850, font_size = 20)
        snd_btn_off.draw(190, 830, screen, c_sound_btn_off)
        snd_btn_off.print_text('ВЫКЛ', 195, 850, font_size = 20)
        sound_text.print_text('ЗВУК:', 10,850, font_size = 20)
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # elif event.type == pygame.USEREVENT:
            #     pygame.quit()
            #     start_g()
run_game()