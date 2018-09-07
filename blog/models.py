from django.db import models
from mongoengine import *
#连接数据库的名字
class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)