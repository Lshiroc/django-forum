from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json

from .forms import NewPostForm
from .models import Tag

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
