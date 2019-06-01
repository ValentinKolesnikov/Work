from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    
    class Meta():
        db_table = 'Work'
    name = models.CharField(max_length = 50)
    text = models.TextField()
    photo = models.ImageField(upload_to='works', blank=True, default = None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)
    fio = models.CharField(max_length = 50, blank=True)

    def __str__(self):
        return self.name

class Like(models.Model):
    class Meta():
        db_table = 'Like'
    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.work.name)
