from django.http import HttpResponse
from django.shortcuts import render, redirect
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
            comment.title = form.cleaned_data['commentid']
            comment.content = form.cleaned_data['comment']
            comment.save()
            return redirect(reverse('toon:detail', kwargs={'toon_id':toon_id}))
    return render(request, 'toon/edit.html', {'form':form})

def toon_delete(request, toon_id):
    toon = Toon.objects.get(titleid = toon_id)
    toon.is_deleted = True
    toon.save()
    return redirect(reverse('toon:index'))

# def toon_category(request):
#     toon = Toon.objects.all()
#     return 


# def toon_create(request):
#     #print(dir(request))

#     form = ToonForm()
#     if request.method == 'POST':
#         form = ToonForm(request.POST)
#         if form.is_valid():
#             # board = Board(
#             #     title = data['title'],
#             #     content = data['content']
#             # )
#             # board.save()
#             form.save(commit=True)
#             return redirect(reverse('toon:index'))
#             #return redirect('/board')

#     return render(request, 'toon/create.html', {'form':form})