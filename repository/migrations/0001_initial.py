# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-26 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('summary', models.CharField(max_length=128, verbose_name='简介')),
                ('detail', models.TextField(verbose_name='文章详情')),
                ('ctime', models.DateTimeField(auto_now=True)),
                ('types', models.IntegerField(choices=[(1, 'Python'), (2, 'OpenStack'), (3, 'GoLang'), (4, 'MySQL')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Article_to_Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surfix', models.CharField(max_length=32, verbose_name='博客后缀')),
                ('theme', models.CharField(max_length=32, verbose_name='主题 ')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('summary', models.CharField(max_length=256, verbose_name='简介')),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='标题')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('ctime', models.DateTimeField(auto_now=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article')),
                ('parent_comment_id', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='FansEachother',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MaintenlanceForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=32, verbose_name='报障单号')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('ctime', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('dtime', models.DateTimeField(null=True, verbose_name='处理时间')),
                ('status', models.IntegerField(choices=[(1, '待处理'), (2, '处理中'), (3, '已完成')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=32, verbose_name='标题')),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Up_Down',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_up', models.BooleanField(default='')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Article')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
            ],
            options={
                'verbose_name': '用户信息表',
            },
        ),
        migrations.AddField(
            model_name='up_down',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='maintenlanceform',
            name='initiator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initiator', to='repository.UserInfo', verbose_name='发起人'),
        ),
        migrations.AddField(
            model_name='maintenlanceform',
            name='processor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processor', to='repository.UserInfo', verbose_name='处理人'),
        ),
        migrations.AddField(
            model_name='fanseachother',
            name='fans_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='f_id', to='repository.UserInfo', verbose_name='粉丝ID'),
        ),
        migrations.AddField(
            model_name='fanseachother',
            name='star_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s_id', to='repository.UserInfo', verbose_name='明星ID'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.UserInfo'),
        ),
        migrations.AddField(
            model_name='article_to_tags',
            name='tags_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.Tags'),
        ),
    ]
