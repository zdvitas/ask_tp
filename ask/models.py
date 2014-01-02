from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    raiting = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User)
    class Meta:
        ordering = ["-pub_date"]

    def __unicode__(self):
        return self.title + ' by ' + self.user.username
    def get_url(self):
        return "/quest%i" % self.id
    def get_usr_url(self):
        return "/user%i" % self.user_id


class Answer(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    raiting = models.IntegerField()
    pub_date = models.DateTimeField('date published')
    quest = models.ForeignKey(Questions)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title




