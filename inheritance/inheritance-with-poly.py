"""
Demostrate inheritance with polymorphism.

Notice how the __init__ method in the parent class is able to access
the ext class variable from different subclasses? That's polymorphism.
If the file_name doesn't end with the correct name, it raises an exception.

The fact that AudioFile doesn't actually store a reference to the ext variable
doesn't stop it from being able to access it on the subclass.

"""
class AudioFile:
    def __init__(self, file_name):
        if not file_name.endswith(self.ext):
            raise Exception("Invalid file format")
        
        self.file_name = file_name

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        pirnt("Playing {} as mp3".format(self.file_name))

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        pirnt("Playing {} as wav".format(self.file_name))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        pirnt("Playing {} as ogg".format(self.file_name))
