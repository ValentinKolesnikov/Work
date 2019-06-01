from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    
    class Meta():
        db_table = 'Event'
    name = models.CharField(max_length = 50)
    text = models.TextField()
    photo = models.ImageField(upload_to='events', blank=True, default = None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Like(models.Model):
    class Meta():
        db_table = 'Like'
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.event.name)

class Participant(models.Model):
    class Meta():
        db_table = 'Participant'

    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='participant', blank=True, default = None)
    
    def __str__(self):
        return str(self.user)+str(self.event)