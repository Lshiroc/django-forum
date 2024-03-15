from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import json

from .forms import NewPostForm, NewComment
from .models import Post, Tag, Comment

@login_required
def upvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post in request.user.upvoted_posts.all():
        post.upvote.remove(request.user)
    else:
        if post in request.user.downvoted_posts.all():
            post.downvote.remove(request.user)
        post.upvote.add(request.user)

    return redirect('post:detail', pk)

@login_required
def downvote_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post in request.user.downvoted_posts.all():
        post.downvote.remove(request.user)
    else:
        if post in request.user.upvoted_posts.all():
            post.upvote.remove(request.user)
        post.downvote.add(request.user)

    return redirect('post:detail', pk)

@login_required
def upvote_comment(request, postid, commentid):
    comment = get_object_or_404(Comment, pk=commentid)
    if comment in request.user.upvoted_comments.all():
        comment.upvotes.remove(request.user)
    else:
        if comment in request.user.downvoted_comments.all():
            comment.downvotes.remove(request.user)
        comment.upvotes.add(request.user)
    comment.save()

    return redirect('post:detail', postid)  

@login_required
def downvote_comment(request, postid, commentid):
    comment = get_object_or_404(Comment, pk=commentid)
    if comment in request.user.downvoted_comments.all():
        comment.downvotes.remove(request.user)
    else:
        if comment in request.user.upvoted_comments.all():
            comment.upvotes.remove(request.user)
        comment.downvotes.add(request.user)
    comment.save()

    return redirect('post:detail', postid)

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    score = post.upvote.count() - post.downvote.count()

    if request.method == 'POST':
        form = NewComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.posted_by = request.user
            comment.post = post
            comment.save()

            return redirect('post:detail', pk)
    else:
        form = NewComment()

    return render(request, 'post/detail.html', {
        'post': post,
        'score': score,
        'form': form,
    })

@login_required
def new(request):
    if request.method == 'POST':
        print(request.POST['tags'])
        form = NewPostForm(request.POST)
        tags = json.loads(request.POST['tags'])['tags']
        tagsModels = []
        for tag in tags:
            tag = Tag.objects.get_or_create(name=tag)[0]
            tagsModels.append(tag)
            print("in for")
        if form.is_valid():
            print("form is valid`")
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
