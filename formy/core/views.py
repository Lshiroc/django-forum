from django.shortcuts import render, redirect

from .forms import SignupForm, LoginForm
from accounts.models import CustomUser

def index(request):
    return render(request, 'core/index.html')


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

def test(request):

    return render(request, 'core/follow_test.html')

def followu2(request):
    request.user.following.add(CustomUser.objects.get(id=3))
    CustomUser.objects.get(id=3).followers.add(request.user)

    return redirect('core:test')
