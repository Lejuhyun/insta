from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta():
        model = Post
        # fields = '__all__'
        fields = ('content', 'image', )

class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ('content', ) # 사용자에게 콘텐츠만 보여줌 
