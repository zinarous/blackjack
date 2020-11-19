import pygame
pygame.init()
WIDTH = 1600
HEIGHT = 900

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")
pygame.display.set_icon(pygame.image.load("icon.png"))
clock = pygame.time.Clock()
background_image = pygame.image.load('background.png')

pygame.mixer.music.load("background_s.mp3")
pygame.mixer.music.set_volume(0.1)
button_sound = pygame.mixer.Sound('but_fat.mp3')




class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (13,162,58)
        self.active_color = (23,204,58)
    def draw(self, x, y, msg, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(screen, self.active_color, (x , y , self.width, self.height))
                if click[0] == 1:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)#временная задержка, чтобы постоянно не проигрывался звук
                    if action is not None:
                        action()
        else:
            pygame.draw.rect(screen, self.inactive_color, (x , y , self.width, self.height))

        print_text(msg, x + 200, y + 200)
def print_text(message, x, y, font_color = (0, 0, 0), font_type = "TNR.ttf", font_size=20):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))
def pause():
    pygame.mixer.music.pause()
button = Button(200, 250)
button.draw(400, 200, 'Start Game!')
pygame.mixer.music.play(-1)
# Цикл игры
running = True # флаг выхода из цикла игры
while running:
    # Отслеживание события: "закрыть окно"
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка закрытия окна
        if event.type == pygame.QUIT:
            running = False
# Выход из игры:
pygame.quit()