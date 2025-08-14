#LUKAZVLYREK
import pygame
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect, QMediaPlayer, QAudioOutput, QAudioDevice
from os import path

class Musica():
    def __init__(self):
        self.efecto = QSoundEffect()
        
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.15)
        directorio = path.abspath(path.join(path.dirname(__file__), '../Assets/Musica')) # ruta donde estan las canciones
        self.menu = directorio + "/ATE.ogg"
        self.board = directorio + "/DK.ogg"
        self.battle = directorio + "/SSBW.ogg"
        self.final = directorio + "/AOE3.mp3"
        self.move = directorio+ "/efecto.wav"

    #STOP MUSIC
    def stopmusic(self):
        pygame.mixer.music.stop()

    #MENU MUSIC
    def play_menu_music(self):
        pygame.mixer.music.load(self.menu)
        pygame.mixer.music.play(-1)

    #TABLERO MUSIC
    def play_tablero_music(self):
        pygame.mixer.music.load(self.board)
        pygame.mixer.music.play(-1)

    #BATTLE MUSIC
    def play_battle_music(self):
        pygame.mixer.music.load(self.battle)
        pygame.mixer.music.play(-1)


    #GAME OVER MUSIC
    def play_game_over_music(self):
        pygame.mixer.music.load(self.final)
        pygame.mixer.music.play(1)

    #EFECT PIECE
    def play_move_effect(self):
        self.efecto.setSource(QUrl.fromLocalFile(self.move))
        self.efecto.play()
    



class Music():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.15)
        self.musica = QMediaPlayer()
        self.musica.setAudioOutput(QAudioOutput().setVolume(0.15))
        self.musica

        directorio = path.abspath(path.join(path.dirname(__file__), '../Assets/Musica')) # ruta donde estan las canciones
        self.menu = directorio + "/ATE.ogg"
        self.board = directorio + "/DK.ogg"
        self.battle = directorio + "/SSBW.ogg"
        self.final = directorio + "/AOE3.mp3"
        self.move = directorio+ "/efecto.wav"
        
        # Efecto de sonido
        self.efecto = QSoundEffect()
        self.efecto.setSource(QUrl.fromLocalFile(self.move))

    #STOP MUSIC
    def stopmusic(self):
        pygame.mixer.music.stop()

    #MENU MUSIC
    def play_menu_music(self):
        self.musica.setSource(QUrl.fromLocalFile(self.board))
        self.musica.play()

        print(self.musica.isPlaying())

        # pygame.mixer.music.load(self.menu)
        # pygame.mixer.music.play(-1)

    #TABLERO MUSIC
    def play_tablero_music(self):
        pygame.mixer.music.load(self.board)
        pygame.mixer.music.play(-1)

    #BATTLE MUSIC
    def play_battle_music(self):
        pygame.mixer.music.load(self.battle)
        pygame.mixer.music.play(-1)


    #GAME OVER MUSIC
    def play_game_over_music(self):
        pygame.mixer.music.load(self.final)
        pygame.mixer.music.play(1)

    #EFECT PIECE
    def play_move_effect(self):
        self.efecto.play()
    
class Test:
    if __name__ == "__main__":
        musica = Music()

        musica.play_move_effect()
        # input
