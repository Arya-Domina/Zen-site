from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')


def picture(request):
    return render(request, 'app/picture.html')


def music(request):
    return render(request, 'app/music.html')


def yoga(request):
    return render(request, 'app/yoga.html')


def game(request):
    return render(request, 'app/game.html')


def fire(request):
    return render(request, 'app/fire.html')


