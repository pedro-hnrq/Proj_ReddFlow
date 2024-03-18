from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from .models import Topic, Comment
from .forms import TopicForm, CommentForm
from .choices import CATEGORY_CHOICES 


def topic_view(request):
    posts_por_pagina = 5
    if request.method == "GET":
        posts = Topic.objects.all()
        assunto = request.GET.get('assunto')
        if assunto:
            posts = posts.filter(subject__icontains=assunto)
        paginator = Paginator(posts, posts_por_pagina)
        pagina = request.GET.get('pagina')
        posts_paginados = paginator.get_page(pagina)
        return render(request, 'topic_view.html', {'posts': posts_paginados})

def new_post(request):
    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post criado com sucesso!')
            return redirect('topic_view')
    else:
        form = TopicForm()
    return render(request, 'new_post.html', {'form': form, 'category_choices': CATEGORY_CHOICES})

def edit_post(request, post_id):
    post = Topic.objects.get(pk=post_id)

    # Verificar se o usuário logado é o autor do post
    if request.user != post.author:
        raise Http404("Você não tem permissão para editar este post.")

    if request.method == 'POST':
        form = TopicForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Post editado com sucesso!')
            return redirect('topic_view')
    else:
        form = TopicForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id):
    post = Topic.objects.get(pk=post_id)

    # Verificar se o usuário logado é o autor do post
    if request.user != post.author:
        raise Http404("Você não tem permissão para excluir este post.")

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post excluído com sucesso!')
        return redirect('topic_view')

    return render(request, 'delete_post.html', {'post': post})


def comment(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.topic = topic  # Definindo o tópico para o comentário
            comment.Commentator = request.user
            comment.save()
            messages.success(request, 'Comentário criado com sucesso!')
            return redirect('comment', topic_id=topic_id)  # Redirecionar com o topic_id
    else:
        form = CommentForm()
    
    comments = Comment.objects.filter(topic=topic)  # Filtrando os comentários pelo tópico
    return render(request, 'comment.html', {'form': form, 'comments': comments, 'topic': topic})