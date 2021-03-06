import pygame
from moviepy.editor import *
import pygame_menu
import math

pygame.init()
surface = pygame.display.set_mode((800, 600))
song_start = pygame.mixer.Sound('Sounds/8bitlong.mp3')
music_logic = 1
size = width, height = 400, 400
FPS = 40
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
table_border = pygame.sprite.Group()
break_border = pygame.sprite.Group()
list_of_break = list()
lenght_of_table = 33
table_x = 180
table_y = 300
flag = True
life = 3
f = open("all_level/now_level.txt", 'w', encoding="utf8")
f.write(str(0))
f.close()
f = open("all_level/now_level.txt", 'r', encoding="utf8")
now_level = int(f.read())

#открывает меню
def start_menu_open():
    pygame.display.set_mode((800, 600))
    StartP = StartPage()
    StartP.menu.mainloop(surface)

#функции управления музыкой
def music_play():
    song_start.stop()
    song_start.play()
    global music_logic
    music_logic = 1


def music_stop():
    song_start.stop()
    global music_logic
    music_logic = 0


def start_game():
    start()

#первый уроень
def first_level():
    temp_x = 10
    temp_y = 20
    for i in range(8):
        for j in range(0, 19, 1):
            if j % 2 == i % 2:
                Brik(temp_x, temp_y)
            temp_x += 20
        temp_y += 20
        temp_x = 10

#второй уровень
def second_level():
    temp_x = 11
    temp_y = 30
    for j in range(6):
        for i in range(18):
            Brik(temp_x, temp_y)
            temp_x += 20 + 1
        temp_x = 11
        temp_y += 30

#третий уровень
def third_level():
    temp_x = 0
    temp_y = 5
    map_level = [
        [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    for i in range(14):
        for j in range(20):
            if map_level[i][j] == 1:
                Brik(temp_x, temp_y)
            temp_x += 20
        temp_y += 20
        temp_x = 0
    Brik(190, 115)


next_level = [first_level, second_level, third_level]

#класс кирпичей
class Brik(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.len = 20
        self.x = x
        self.y = y
        self.image = pygame.Surface((2 * 20, 2 * 20), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color("blue"),
                         (0, 0, 20, 20))
        self.rect = pygame.Rect((x, y, 20, 20))
        self.add(break_border)

#класс доски
class Table(pygame.sprite.Sprite):
    def __init__(self, length):
        super().__init__(all_sprites)
        self.len = length
        self.image = pygame.Surface((2 * length, 2 * length), pygame.SRCALPHA, 32)
        pygame.draw.rect(self.image, pygame.Color("white"),
                         (0, 0, length, 15))
        self.rect = pygame.Rect((180, 300, length, 15))
        self.add(table_border)
        self.v = 0

    def update(self):

        global table_x
        self.rect = self.rect.move(self.v, 0)
        table_x += self.v
        #взаимодействие с границами поля
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.v = 0
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.v = 0

#класс мяча
class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.first_start = True
        self.vx = 0
        self.vy = 0

    def update(self):
        global height
        global flag
        self.rect = self.rect.move(self.vx, self.vy)
        #взаимодействие с границами поля
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            if self.rect.y > 355:
                flag = False
                self.vy = 0
                self.vx = 0
            else:
                self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
        #взаимодействие с доской
        if pygame.sprite.spritecollideany(self, table_border):
            p_vx = min(lenght_of_table / 2, abs(self.rect.x + self.radius - table_x - lenght_of_table / 2))
            p_vy = math.sqrt((lenght_of_table ** 2) / 2 - (lenght_of_table / 2) ** 2)
            p_c = math.sqrt(p_vx ** 2 + p_vy ** 2)
            kf = 5 / p_c
            self.vx = p_vx * kf
            self.vy = p_vy * kf * (-1)
            if self.rect.x + self.radius - table_x - lenght_of_table / 2 < 0:
                self.vx *= -1
        #взаимодействие с кирпичиками
        if pygame.sprite.spritecollideany(self, break_border):
            gets_hit = pygame.sprite.spritecollideany(self, break_border)
            if gets_hit.x <= self.rect.x <= gets_hit.x + 20:
                self.vy = -self.vy
            if gets_hit.y <= self.rect.y <= gets_hit.y + 20:
                self.vx = -self.vx
            for some_sprite in break_border:
                # print(some_sprite)
                if gets_hit == some_sprite:
                    break_border.remove(some_sprite)
                    some_sprite.kill()

#класс стенок игрового поля
class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)

#класс стартовой страницы
class StartPage():
    menu = pygame_menu.Menu(600, 800, 'Arcanoid', theme=pygame_menu.themes.THEME_DARK)
    menu.add_button('Музыка Вкл', music_play)
    menu.add_button('Музыка Выкл', music_stop)
    menu.add_label('')
    menu.add_label('')
    menu.add_button('Играть', start_game)
    menu.add_label('')
    menu.add_button('Выйти', pygame_menu.events.EXIT)

#класс траници при проигрыше
class ReturnPage():
    menu = pygame_menu.Menu(600, 800, 'Arcanoid', theme=pygame_menu.themes.THEME_DARK)
    menu.add_button('Музыка Вкл', music_play)
    menu.add_button('Музыка Выкл', music_stop)
    menu.add_label('')
    menu.add_label('')
    menu.add_button('Попробовать еще раз)', start_game)
    menu.add_label('')
    menu.add_button('Выйти', pygame_menu.events.EXIT)

#функция с игровым циклом
def start():
    global life
    global flag
    global table_x
    global now_level
    global music_logic

    pygame.init()
    pygame.display.set_caption('Arcanoid')

    if music_logic == 1:
        song_start.stop()
        song_start.play()

    screen = pygame.display.set_mode(size)
    screen.fill('black')
    running = True
    ball = Ball(15, 180, 269)
    table = Table(lenght_of_table)
    clock = pygame.time.Clock()
    Border(10, 10, width - 10, 10)
    Border(10, height - 10, width - 10, height - 10)
    Border(10, 10, 10, height - 10)
    Border(width - 10, 10, width - 10, height - 10)
    next_level[now_level]()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.QUIT:
                ball.kill()
                table.kill()
                for i in break_border:
                    i.kill()
                start_menu_open()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ball.first_start is True:
                    ball.vy = -5
                    ball.first_start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if ball.first_start is True:
                        ball.vx = 2
                    table.v = 2
                if event.key == pygame.K_LEFT:
                    if ball.first_start is True:
                        ball.vx = -2
                    table.v = -2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    if ball.first_start is True:
                        ball.vx = 0
                    table.v = 0
                if event.key == pygame.K_LEFT:
                    if ball.first_start is True:
                        ball.vx = 0
                    table.v = 0
        table_x = table.rect.x
        if ball.first_start is True:
            ball.rect = ball.rect.move(table.rect.x - ball.rect.x, 269 - ball.rect.y)
        all_sprites.update()
        screen.fill('black')
        all_sprites.draw(screen)
        pygame.display.flip()
        if flag is False:
            #если все жизни кончились да или нет
            if life > 0:
                #вернуть все на свое место
                table.rect = table.rect.move(180 - table.rect.x, 0)
                ball.rect = ball.rect.move(table.rect.x - ball.rect.x, 269 - ball.rect.y)
                flag = True
                life -= 1
                ball.first_start = True
            else:
                #вывести вкладку о конце игры
                #записать количество жизней в 3
                f = open("all_level/now_level.txt", 'w', encoding="utf8")
                f.write(str(0))
                f.close()
                for i in break_border:
                    i.kill()
                now_level = 0
                flag = True
                ball.first_start = True
                ball.rect = ball.rect.move(180 - ball.rect.x, 100 - ball.rect.y)
                life = 3
                ball.kill()
                table.kill()
                pygame.init()
                pygame.display.set_mode((800, 600))
                ReturnP = ReturnPage()
                ReturnP.menu.mainloop(surface)
        if len(break_border) == 0:
            #если все кирпичи разбиты
            f = open("all_level/now_level.txt", 'w', encoding="utf8")
            f.write(str(now_level + 1))
            f.close()
            now_level += 1
            if now_level == 3:
                f = open("all_level/now_level.txt", 'w', encoding="utf8")
                f.write(str(0))
                f.close()
                pygame.display.set_mode((800, 600))
                WinP = WinPage()
                WinP.menu.mainloop(surface)
                # окно Вы выйграли
                # переход на вкладку с меню
            else:
                ball.first_start = True
                ball.rect = ball.rect.move(180 - ball.rect.x, 100 - ball.rect.y)
                life = 3
                ball.kill()
                table.kill()
                # вкладка следующий уровень (уровень 2 или 3 в обще n)
                pygame.display.set_mode((800, 600))
                NextLevelP = NextLevelPage()
                NextLevelP.menu.mainloop(surface)
                next_level[now_level]()
            table.rect = table.rect.move(180 - table.rect.x, 0)
            ball.rect = ball.rect.move(table.rect.x - ball.rect.x, 269 - ball.rect.y)
            flag = True
            life -= 1
            ball.first_start = True


#класс странице переходной между уровнями
class NextLevelPage():
    menu = pygame_menu.Menu(600, 800, 'Arcanoid', theme=pygame_menu.themes.THEME_DARK)
    menu.add_button('Музыка Вкл', music_play)
    menu.add_button('Музыка Выкл', music_stop)
    menu.add_label('')
    menu.add_label('Вы прошли текущий уровень! Поздравляем!')
    menu.add_label('')
    menu.add_button('Следующий уровень', start_game)
    menu.add_button('В меню', start_menu_open)
    menu.add_button('Выйти', pygame_menu.events.EXIT)

#класс страницы при выигрывании
class WinPage():
    menu = pygame_menu.Menu(600, 800, 'Arcanoid', theme=pygame_menu.themes.THEME_DARK)
    menu.add_button('Музыка Вкл', music_play)
    menu.add_button('Музыка Выкл', music_stop)
    menu.add_label('')
    menu.add_label('Поздравляем! Вы Выиграли!')
    menu.add_label('')
    menu.add_button('В меню', start_game)


if __name__ == '__main__':
    pygame.display.set_caption('Arcanoid')
    clip = VideoFileClip(r"media/StartMovie86.mp4")
    clip.preview()
    song_start.play()
    start_menu_open()
