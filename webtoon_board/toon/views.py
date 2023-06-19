from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Toon, Comment, User
from .forms import CommentForm, ToonForm
from django.db.models import Prefetch
from django.urls import reverse

def index(request):
    toon_list = Toon.objects.all()
    return render(request, 'toon/index.html',
                    {"toon_list" : toon_list})

def toon_detail(request, toon_id):
    toon = Toon.objects.prefetch_related('author').get(titleid=toon_id)

    comment_set = toon.comment_set.prefetch_related('user').all()[:10]

    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment(content = data['content'], toon=toon)
            comment.save()
        return redirect(reverse('toon:detail', kwargs={'toon_id':toon_id}))

    return render(request, 'toon/detail.html', 
    {'toon':toon, 'form':form, 'comment_set': comment_set})

def toon_edit(request, toon_id):
    comment = Comment.objects.get(commentid=toon_id)
    form = ToonForm(initial={
        'title':comment.commentid,
        'content':comment.comment,
    })
    if request.method == 'POST':
        form = ToonForm(request.POST)
        if form.is_valid():
            comment.comment = form.cleaned_data['comment']
            comment.save()
            return redirect(reverse('toon:detail', kwargs={'toon_id':toon_id}))
    return render(request, 'toon/edit.html', {'form':form})

def toon_delete(request, toon_id):
    comment = get_object_or_404(Comment, commentid = toon_id)
    if request.method == 'POST':
        comment.delete()
        return redirect(reverse('toon:detail'))
    else:
        return redirect(reverse('toon:detail'))