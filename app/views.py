from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests
from social_django import models


@login_required
def index(request):
    user = models.UserSocialAuth.objects.get(user=request.user)
    response = requests.get(url='https://api.vk.com/method/friends.get?count=5&fields=city,domain&'
                                'access_token=15bbd28623aa9ea5f2510e85330289ca2ae8c3ceae8e2606d9dd'
                                '50ca76d4cc74a0cc11c9a718aa7899d1c&v=V')
    friends = response.json()['response']
    for friend in friends:
        print(friend)

    return render(request, 'app/index.html', {'image': user.extra_data['photo_200_orig'], 'friend': friends},)
