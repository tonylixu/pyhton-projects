class AudioFile:
    def __init__(self, file_name):
        if not file_name.endswith(self.ext):
            raise Exception("Invalid file format")
        
        self.file_name = file_name

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        pirnt("Playing {} as mp3".format(self.file_name))
