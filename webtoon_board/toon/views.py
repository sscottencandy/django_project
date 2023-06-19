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

def toon_edit(request, comment_id):
    comment = Comment.objects.get(commentid=comment_id)
    form = ToonForm(initial={
        'title':comment.commentid,
        'content':comment.comment,
    })
    if request.method == 'POST':
        form = ToonForm(request.POST)
        if form.is_valid():
            comment.comment = form.cleaned_data['comment']
            comment.save()
            return redirect(reverse('toon:detail', kwargs={'comment_id':comment_id}))
    return render(request, 'toon/edit.html', {'form':form})


from django.http import HttpRequest
def toon_delete(request:HttpRequest, comment_id):
    comment = get_object_or_404(Comment, commentid = comment_id)
    if request.method == 'POST':
        comment.delete()
    return redirect(request.headers['Referer'])

# from django.contrib.auth.decorators import login_required
# @login_required
# def comment_like(request, comment_id):
#     post = get_object_or_404(Post, id=comment_id)
#     user = request.user
#     comment = Comment.objects.get(user=user)

#     check_like_post = comment.like_posts.filter(id=comment_id)

#     comment.like_posts.add(post)
#     post.like_count += 1
#     post.save()

#     return redirect('toon:detail', comment_id)