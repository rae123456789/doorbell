from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Borough(models.Model):
    bname = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.bname

class Group(models.Model):
    group = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.group

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borough = models.ForeignKey(Borough, on_delete=models.DO_NOTHING)
    groups = models.ManyToManyField(Group)

    def __str__(self) -> str:
        return f'{self.user.username} ({self.borough.bname})'


class Post(models.Model):
    post_text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete = models.DO_NOTHING )
    group = models.ForeignKey(Group, on_delete = models.DO_NOTHING )
    borough = models.ForeignKey(Borough, on_delete = models.DO_NOTHING )
    likers = models.ManyToManyField(User, related_name='doorbell_likers')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.post_text


class PostReply(models.Model):
    reply_text = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete = models.DO_NOTHING )
    reply_likers = models.ManyToManyField(User, related_name='reply_likers')
    pub_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
