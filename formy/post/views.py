from django.shortcuts import render, redirect
import json

from .forms import NewPostForm
from .models import Tag

def new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.posted_by = request.user
            tags = json.loads(request.POST['tags'])['tags']
            tagsModels = []
            for tag in tags:
                tag = Tag.objects.get_or_create(name=tag)
                tagsModels.append(tag)

            form.tags = tagsModels
            form.save()
            return redirect('/')
    else:
        form = NewPostForm()

    return render(request, 'post/new.html', {
        'form': form
    })
