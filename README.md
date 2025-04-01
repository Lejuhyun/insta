# 댓글 기능 구현하기
## 0. 설치해야하는 것들
```shell
pip install -r requirements.txt 
```
## 1. url 달기
```python 
path('<int:post_id>/comments/create/', views.comment_create, name='comment_create'),
```

## 2. form 만들기 (forms.py)
```python
from .models import Comment
class CommentForm(ModelForm):
    class Meta():
        model = Comment
        fields = ('content', ) 
```

## 3. views 수정하기(views.py)
```python
from .forms import CommentForm
def index(request):
    posts = Post.objects.all()
    form = CommentForm()
    context ={
        'posts': posts,
        'form': form,
    }

    return render(request, 'index.html', context)
```

## 4. index.html은 card.html을 참조하고 있으므로 card.html 수정하기
```html
{% load django_bootstrap5 %}
    <div class="card-footer">
      <form action="{% url 'posts:comment_create' post.id %}" method = "POST">
        <div class="row">
          <div class = "col-9">
            {% bootstrap_form form show_label=False %}
          </div>
          <div class = "col-2">
            <input type="submit" class="btn btn-primary">
          </div>
        </div>
      </form>
    </div>
```
- <div class ="row"> : 댓글입력form과 제출버튼을 하나의 row로 설정한ek => 12칸으로 나눔
    - 입력칸과 submit 버튼을 각각 div로 묶는다
    - <div class = "col-9">: 입력칸은 9개의 칸을 차지하도록
    - <div class = "col-2">: submit버튼은 2개의 칸을 차지하도록
- {% bootstrap_form form show_label=False wrapper_class='' %}
    - show_label=False: content라는 라벨을 안보이게 해준다
    - wrapper_class='': 아래쪽 여백 없애준다

- 부트스트랩 그리드시스템 : 12개의 칸으로 나눈다(얼마의 영역을 차지할지 결정해준다)

## 5. views생성해준다
```python
@login_required
def comment_create(request, post_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False) # 임시저장만 해줌
        comment.user = request.user # 댓글 입력한 사람
        comment.post_id = post_id 
        comment.save()
        return redirect('posts:index')
```