from django.db import models
from django.contrib.auth.models import AbstractUser,User
# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32,verbose_name="用户名",unique=True,null=False)
    password = models.CharField(max_length=32,verbose_name="密码")
    email = models.CharField(max_length=32,verbose_name="邮箱")

    class Meta:
        verbose_name = "用户信息表"

class Blog(models.Model):
    surfix = models.CharField(max_length=32,verbose_name="博客后缀")
    theme = models.CharField(max_length=32,verbose_name="主题 ")
    title = models.CharField(max_length=32,verbose_name="标题")
    summary = models.CharField(max_length=256,verbose_name="简介")
    user = models.OneToOneField(to="UserInfo")

class FansEachother(models.Model):
    star_id = models.ForeignKey(to="UserInfo",related_name="s_id",verbose_name="明星ID")
    fans_id = models.ForeignKey(to="UserInfo",related_name="f_id",verbose_name="粉丝ID")

class MaintenlanceForm(models.Model):
    uuid = models.CharField(max_length=32,verbose_name="报障单号")
    title = models.CharField(max_length=32,verbose_name="标题")
    ctime = models.DateTimeField(auto_now=True,verbose_name="创建时间")
    dtime = models.DateTimeField(verbose_name="处理时间",null=True)
    initiator = models.ForeignKey(to="UserInfo",related_name="initiator",verbose_name="发起人")
    processor = models.ForeignKey(to="UserInfo",related_name="processor",verbose_name="处理人")
    status_choices = (
        (1,"待处理"),
        (2,"处理中"),
        (3,"已完成"),
    )
    status = models.IntegerField(choices=status_choices,default=1,null=False)

class Classify(models.Model):
    caption = models.CharField(max_length=32,verbose_name="标题")
    bid = models.ForeignKey(to="Blog")

    def __str__(self):
        return self.caption

class Tags(models.Model):
    caption = models.CharField(max_length=32,verbose_name="标题")
    bid = models.ForeignKey(to="Blog")

    def __str__(self):
        return self.caption

class Article(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=32,verbose_name="标题")
    summary = models.CharField(max_length=128,verbose_name="简介")
    detail = models.TextField(verbose_name="文章详情")
    ctime = models.DateTimeField(auto_now=True)
    type_of_article = (
        (1,"Python"),
        (2,"OpenStack"),
        (3,"GoLang"),
        (4,"MySQL"),
    )
    types = models.IntegerField(choices=type_of_article,default=1)

class Article_to_Tags(models.Model):
    # id = models.AutoField()
    article_id = models.ForeignKey(to="Article")
    tags_id = models.ForeignKey(to="Tags")

class Comment(models.Model):
    # id = models.AutoField()
    content = models.TextField()
    user = models.ForeignKey(to="UserInfo")
    ctime = models.DateTimeField(auto_now=True,null=False)
    parent_comment_id = models.ForeignKey(to="Comment",null=True,default="")
    article = models.ForeignKey(to="Article")

class Up_Down(models.Model):
    # id = models.AutoField()
    article_id = models.ForeignKey(to="Article")
    user_id = models.ForeignKey(to="UserInfo")
    is_up = models.BooleanField(default="")
    #联合唯一索引

