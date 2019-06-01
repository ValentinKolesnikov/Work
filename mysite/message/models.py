from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Chat(models.Model):
    class Meta():
        db_table = 'Chat'

    members = models.ManyToManyField(User)

    def companion(self, user):
        print('das')
        for u in self.members.all():
            if u != user:
                return u
        return None

    def __str__(self):
        ret = ''
        for u in self.members.all():
            ret+= str(u)+' '
        return ret

class Message(models.Model):
    class Meta():
        db_table = 'Message'

    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.TextField()
    user_from = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

