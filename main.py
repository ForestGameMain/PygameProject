import sys
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1280, 720))
song_start = pygame.mixer.Sound('Sounds/8bitlong.mp3')
music_logic = 1

class MainGame():
    def start_class():
        song_start.stop()
        pygame.quit()
        pygame.init()
        if music_logic == 1:
            song_start.play()
        pygame.display.set_mode((1280, 720))
        # сама игра


class StartPage():
    def music_play():
        song_start.play()
        global music_logic
        music_logic = 1

    def music_stop():
        song_start.stop()
        global music_logic
        music_logic = 0

    def start_game():
        MainGame.start_class()

    menu = pygame_menu.Menu(720, 1280, 'Arcanoid', theme=pygame_menu.themes.THEME_DARK)
    menu.add_button('Музыка Вкл', music_play)
    menu.add_button('Музыка Выкл', music_stop)
    menu.add_label('')
    menu.add_label('')
    menu.add_button('Играть', start_game)
    menu.add_label('')
    menu.add_button('Выйти', pygame_menu.events.EXIT)


if __name__ == '__main__':
    StartP = StartPage()
    StartP.menu.mainloop(surface)
