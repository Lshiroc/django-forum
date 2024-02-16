from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import json

from .forms import NewPostForm
from .models import Post, Tag

@login_required
def upvote(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post in request.user.upvoted_posts.all():
        post.upvote.remove(request.user)
    else:
        if post in request.user.downvoted_posts.all():
            post.downvote.remove(request.user)
        post.upvote.add(request.user)

    return redirect('post:detail', pk)

@login_required
def downvote(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post in request.user.downvoted_posts.all():
        post.downvote.remove(request.user)
    else:
        if post in request.user.upvoted_posts.all():
            post.upvote.remove(request.user)
        post.downvote.add(request.user)

    return redirect('post:detail', pk)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    score = post.upvote.count() - post.downvote.count()

    return render(request, 'post/detail.html', {
        'post': post,
        'score': score,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        tags = json.loads(request.POST['tags'])['tags']
        tagsModels = []
        for tag in tags:
            tag = Tag.objects.get_or_create(name=tag)[0]
            tagsModels.append(tag)

        if form.is_valid():
            form.instance.posted_by = request.user
            instance = form.save(commit=False)
            instance.save()
            instance.tags.set(tagsModels)
            return redirect('/')
    else:
        form = NewPostForm()

    return render(request, 'post/new.html', {
        'form': form
    })
