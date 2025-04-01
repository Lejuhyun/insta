from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    form = CommentForm()
    context ={
        'posts': posts,
        'form': form,
    }

    return render(request, 'index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)

@login_required
def comment_create(request, post_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False) # 임시저장만 해줌
        comment.user = request.user # 댓글 입력한 사람
        comment.post_id = post_id 
        comment.save()
        return redirect('posts:index')

def like(request, post_id):
    user = request.user
    post =Post.objects.get(id=post_id)

    # if post in user.like_posts.all():
    if user in post.like_users.all(): # 게시물에 좋아요 버튼 누른사람들에 대한 리스트
        # user.like_posts.remove(post)
        post.like_users.remove(user) # 좋아요 버튼 누른 목록에 유저를 삭제한다
    else:
        # user.like_posts.add(post)
        post.like_users.add(user) # 좋아요 버튼을 누른 목록에 user를 추가한다
    return redirect('posts:index')
