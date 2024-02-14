from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignupForm, LoginForm
from accounts.models import CustomUser
from post.models import Post

def index(request):
    posts = Post.objects.all()
    # tags = get_object_or_404(Post, id=19).tags.all()
    # print(tags)
    # posts = Post.objects.filter(id=17)

    return render(request, 'core/index.html', {
        'posts': posts,
    })


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
