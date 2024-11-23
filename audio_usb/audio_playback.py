import pygame as pg
import threading as th

class Audio:
    def __init__(self):
        pg.mixer.init()

    def play(self, audio_name):
        self.file_path = f"files/{audio_name}.mp3"

        self.audio_thread = th.Thread(target=self._play_audio).start()

    def _play_audio(self):
        
        try:
            pg.mixer.music.load(self.file_path)
            pg.mixer.music.play()
            
            while pg.mixer.music.get_busy():
                pg.time.Clock().tick(10)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def stop(self):
        pg.mixer.music.stop()

    def __del__(self):
        pg.mixer.quit()


audio = Audio()

file_name = input()

audio.play(file_name)
