from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json

from .forms import NewPostForm
from .models import Tag

@login_required
def new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        form.instance.posted_by = request.user
        tags = json.loads(request.POST['tags'])['tags']
        tagsModels = []
        for tag in tags:
            tag = Tag.objects.get_or_create(name=tag)
            tagsModels.append(tag)
        form.tags = tagsModels

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NewPostForm()

    return render(request, 'post/new.html', {
        'form': form
    })
