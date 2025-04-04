from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField

# Create your models here.
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile'
    )
    # post_set(FK) 장고가 자동으로 만들어줌
    # post_set(MMF) 장고가 자동으로 만들어주려함 
    # 역참조 중복 발생 = > 충돌이 발생함
    # post_set => like_posts (MMF)
    followings = models.ManyToManyField('self', related_name='followers', symmetrical = False)
