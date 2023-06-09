from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Board, Comment
from .forms import BoardForm, CommentForm

from django.urls import reverse

def index(request):
    board_list = Board.objects.filter(is_deleted = 0).all()
    return render(request, 'board/index.html',
                    {"board_list" : board_list})

def board_detail(request, board_id):
    board = Board.objects.filter(is_deleted = 0).prefetch_related('comment_set').get(id=board_id)
    #comment_list = Comment.object.filter(board_id=board_id).all()
    
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            comment = Comment(content = data['content'], board=board)
            comment.save()
        return redirect(reverse('board:detail', kwargs={'board_id':board_id}))

    return render(request, 'board/detail.html', {'board':board, 'form':form})

def board_create(request):
    #print(dir(request))

    form = BoardForm()
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            # board = Board(
            #     title = data['title'],
            #     content = data['content']
            # )
            # board.save()
            form.save(commit=True)
            return redirect(reverse('board:index'))
            #return redirect('/board')

    return render(request, 'board/create.html', {'form':form})

def board_edit(request, board_id):
    board = Board.objects.filter(is_deleted = 0).get(id=board_id)
    form = BoardForm(initial={
        'title':board.title,
        'content':board.content
    })
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board.title = form.cleaned_data['title']
            board.content = form.cleaned_data['content']
            board.save()
            return redirect(reverse('board:detail', kwargs={'board_id':board_id}))
    return render(request, 'board/edit.html', {'form':form})

def board_delete(request, board_id):
    board = Board.objects.get(id = board_id)
    board.is_deleted = True
    board.save()
    #board.delete()
    return redirect(reverse('board:index'))