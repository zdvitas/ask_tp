from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title + ' by ' + self.user.username


class Answer(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    quest = models.ForeignKey(Questions)

    def __unicode__(self):
        return self.title




