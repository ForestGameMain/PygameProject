import sys
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1280, 720))
song_start = pygame.mixer.Sound('Sounds/8bitlong.mp3')


class StartPage():
    def set_difficulty(value, difficulty):
        # Локация дано 1,2,3 можно потом где то применить
        pass

    def start_the_game():
        print("START")
        # Сюда писать поссылки на саму игру внутри или сам код
        pass

    def music_play():
        song_start.play()

    def music_stop():
        song_start.stop()

    menu = pygame_menu.Menu(720, 1280, 'Arcanoid', theme=pygame_menu.themes.THEME_DARK)
    menu.add_button('Музыка Вкл', music_play)
    menu.add_button('Музыка Выкл', music_stop)
    menu.add_label('')
    menu.add_text_input('Ваше имя : ', default='someone name')
    menu.add_label('')
    menu.add_selector("Локация : ", [('название карты 1', 1), ('название карты 2', 2), ('название карты 3', 2)],
                      onchange=set_difficulty)
    menu.add_button('Играть', start_the_game)
    menu.add_button('Выйти', pygame_menu.events.EXIT)


if __name__ == '__main__':
    StartP = StartPage()
    StartP.menu.mainloop(surface)
