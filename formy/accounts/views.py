from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import UserProfileChange

@login_required
def profile(request):
    form = UserProfileChange()

    return render(request, 'accounts/profile.html', {
        'form': form,
    })

