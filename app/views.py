from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import requests
from social_django import models


@login_required
def index(request):
    user = get_object_or_404(models.UserSocialAuth, user=request.user)

    response = requests.get(url='https://api.vk.com/method/friends.get?count=5&fields=domain&'
                            'access_token='+user.extra_data['access_token']+'&v=V')

    if response.status_code == 200 and 'response' in response.json():
        friends = response.json()['response']
    else:
        friends = []

    return render(request, 'app/index.html', {'image': user.extra_data['photo_200_orig'], 'friends': friends},)
