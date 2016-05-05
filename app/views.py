from django.shortcuts import render, get_object_or_404
from .models import YogaPost


def index(request):
    return render(request, 'app/index.html')


def picture(request):
    return render(request, 'app/picture.html')


def music(request):
    return render(request, 'app/music.html')


def yoga(request):
    posts = YogaPost.objects.all()
    return render(request, 'app/yoga.html', {'posts': posts})


def post_detail(request, pky):
    post = get_object_or_404(YogaPost, pk=pky)
    return render(request, 'app/post_detail.html', {'post': post})


def game(request):
    return render(request, 'app/game.html')


def fire(request):
    return render(request, 'app/fire.html')


