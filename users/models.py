from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length = 50,blank=True) # 昵称 设置blank=True时 注册时可以不填昵称

    class Meta(AbstractUser.Meta):
        pass