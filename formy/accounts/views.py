from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import UserProfileChange

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileChange(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileChange()

    return render(request, 'accounts/profile.html', {
        'form': form,
    })

