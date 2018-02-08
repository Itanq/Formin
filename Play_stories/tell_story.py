
import os
import json
import pygame
from aip import AipSpeech
from Play_stories.utility import Text

class TextToVoice():
    def __init__(self, path):

        self.APP_ID = '9722405'
        self.API_KEY = 'tZbaIyERxW7kwFYFuahW8AAt'
        self.SECRET_KEY = 'f7ebef906ae105eff896f5bd808c27c4'

        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

        self.res_path = "../Data/voice"
        self.text = Text(path)

        self.iterator_all_stories()


    def make_voice(self, text, resmap3):

        result = self.client.synthesis(text, 'zh', 1, {'vol': 5, })

        if not isinstance(result, dict):
            with open(resmap3, 'wb') as f:
                f.write(result)

    def make_map3(self, file):

        text = open(file, 'r')
        data = json.load(text)

        title = data['title']
        voi = self.res_path + "/" + title + ".mp3"

        if not os.path.exists(voi):
            author = data['author']
            content = self.text.remove_error_symbol(data['content'])
            print("合成音频文件: ", title+".mp3")
            self.make_voice(content, voi)

    def iterator_all_stories(self):
        for f in self.text.story_file:
            self.make_map3(f)

    def play(self, file):
        pygame.mixer.init(frequency=16000, size=-16, channels=4)
        track = pygame.mixer.music.load(self.res_path + "/" + file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.delay(1)
        pygame.mixer.quit()


if __name__ == '__main__':
    test = TextToVoice("/home/zmant/GITHUB/Formin/Data/stories")
    #test.play("森林女孩与兔嘴男孩.mp3")

