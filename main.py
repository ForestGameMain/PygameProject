import sys
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1280, 720))


class StartPage():
    def set_difficulty(value, difficulty):
        # Локация дано 1,2,3 можно потом где то применить
        pass

    def start_the_game():
        # Сюда писать поссылки на саму игру внутри или сам код
        pass

    def music_off_on(value, difficulty):
        if value == 1:
            pygame.mixer.unpause()
        elif value == 0:
            pygame.mixer.pause()

    menu = pygame_menu.Menu(720, 1280, 'Название игры', theme=pygame_menu.themes.THEME_DARK)
    menu.add_selector("Музыка : ", [('Вкл', 1), ('Выкл', 0)], onchange=music_off_on)
    menu.add_text_input('Ваше имя :', default='someone name')
    menu.add_selector("Локация :", [('название карты 1', 1), ('название карты 2', 2), ('название карты 3', 2)],
                      onchange=set_difficulty)
    menu.add_button('Играть', start_the_game)
    menu.add_button('Выйти', pygame_menu.events.EXIT)

    song = pygame.mixer.Sound('Sounds/8bitlong.mp3')
    song.play()


if __name__ == '__main__':
    StartP = StartPage()
    StartP.menu.mainloop(surface)
