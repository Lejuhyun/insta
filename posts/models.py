from django.db import models
from django_resized import ResizedImageField
from django.conf import settings

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='image')
    image = ResizedImageField(
        size=[500, 500], 
        crop=['middle', 'center'],
        upload_to='image/%Y/%m'
    )
    # 작성자
    user = models.ForeignKey( # 1-N 관계설정
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    # 이 글에 좋아요를 누른 사람
    like_users = models.ManyToManyField( # M-N 관계설정
        settings.AUTH_USER_MODEL,# user라는 친구와 post라는 친구를 연결하고 싶음
        related_name = 'like_posts', # 역참조의 중복 발생을 방지하기 위해!!! (작성자도 post_set이고 좋아요 누른 사람도 post_set이라서)
    ) 

class Comment(models.Model):
    content = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
