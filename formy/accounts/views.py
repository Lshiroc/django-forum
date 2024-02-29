from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from PIL import Image
import json

from .forms import UserProfileChange

@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileChange(request.POST)
        print(request.FILES['profile_picture_full'])

        data = request.POST['crop_details']
        cropDetails = json.loads(data)
        # print(img)
        print(request.FILES['profile_picture_full'])
        img = Image.open(request.FILES['profile_picture_full'])
        width, height = img.size
        print(cropDetails)
        img.crop((cropDetails['x'], cropDetails['y'], width*cropDetails['scale'], height*cropDetails['scale']))
        form.instance.profile_picture.save(request.FILES['profile_picture_full'], img.read(), True)
       
        if form.is_valid():
            print("valid")
            
            # form.save()
        else:
            print("it is not valid")
    else:
        form = UserProfileChange()

    return render(request, 'accounts/profile.html', {
        'form': form,
    })

