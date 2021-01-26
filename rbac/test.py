from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

class Role(models.Model):
    caption = models.CharField(max_length=32)

class User2Role(models.Model):
    u = models.ForeignKey(User)
    r = models.ForeignKey(Role)

class Action(models.Model):
    #get
    #post
    #delete
    #change
    caption = models.CharField(max_length=32)

class Permission(models.Model):
    url = models.CharField(max_length=64)

class Permission2Action(models.Model):
    p = models.ForeignKey(Permission)
    a = models.ForeignKey(Action)