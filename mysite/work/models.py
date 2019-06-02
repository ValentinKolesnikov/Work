from django.db import models
from django.contrib.auth.models import User
import os

class Work(models.Model):
    
    class Meta():
        db_table = 'Work'
    name = models.CharField(max_length = 50)
    text = models.TextField()
    photo = models.ImageField(upload_to='works', blank=True, default = None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)
    fio = models.CharField(max_length = 50, blank=True)
    document = models.FileField(upload_to='documents', blank = True)

    def extension(self):
        if not self.document:
            return 'none'
        name, extension = os.path.splitext(self.document.name)
        if extension in ['.3g2', '.3gp', '.3gp2', '.3gpp', '.3gpp2', '.asf', '.asx', '.avi', '.bin',
         '.dat', '.drv', '.f4v', '.flv', '.gtp', '.h264', '.m4v', '.mkv', '.mod', '.moov', '.mov',
          '.mp4', '.mpeg', '.mpg', '.mts', '.rm', '.rmvb', '.spl', '.srt', '.stl', '.swf', '.ts',
           '.vcd', '.vid', '.vob', '.webm', '.wm', '.wmv', '.yuv']:
           return 'video'
        elif extension in ['.wav', '.aif', '.mp3', '.mid']:
            return 'audio'
        else:
            return 'other'

    def __str__(self):
        return self.name

class Like(models.Model):
    class Meta():
        db_table = 'Like'
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.work.name)
