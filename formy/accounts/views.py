from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from PIL import Image
import json

from .forms import UserProfileChange

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileChange(request.POST, request.FILES)
        if form.is_valid():
            data = request.POST['crop_details']
            cropDetails = json.loads(data)
            img = Image.open(request.FILES['profile_picture_full'])
            width, height = im.size
            img.crop((cropDetails.x, cropDetails.y, width*cropDetails.scale, height*cropDetails.scale))
            print(cropDetails)
            
            # form.save()
        else:
            print("it is not valid")
    else:
        form = UserProfileChange()

    return render(request, 'accounts/profile.html', {
        'form': form,
    })

