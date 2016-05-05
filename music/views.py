from django.shortcuts import render, render_to_response, get_object_or_404
from django.template.context_processors import csrf
from music.models import MusicPost, Musical


def articles(request):
    args = {}
    args['posts'] = MusicPost.objects.all()
    return render_to_response('music/music.html', args)


def post_detail(request, pkm):
    post = get_object_or_404(MusicPost, pk=pkm)
    id = post.id
    table = Musical.objects.filter(title_id=id).order_by('name')
    a = dict(posts=table, post=post)
    return render(request, 'music/m.html', a)
