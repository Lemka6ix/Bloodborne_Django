from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ReviewForm, CommentForm, BlogForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import user_passes_test


def index(request):
    return render(request, 'main/index.html')


def resources(request):
    return render(request, 'main/resources.html')


def about(request):
    return render(request, 'main/about.html')


def pool(request):
    form = ReviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data

        return render(request, 'main/pool.html', {
            'form': form,
            'data': data,
            'success': True
        })

    return render(request, 'main/pool.html', {
        'form': form,
        'success': False
    })


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('login')

    return render(request, 'main/register.html', {
        'form': form
    })

def blog(request):
    posts = Blog.objects.all().order_by('-pub_date')
    return render(request, 'main/blog.html', {'posts': posts})


def blogpost(request, parameter):
    post = get_object_or_404(Blog, id=parameter)
    comments = post.comments.select_related('author').order_by('-date')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            return redirect('blogpost', parameter=post.id)
    else:
        form = CommentForm()

    return render(request, 'main/blogpost.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@user_passes_test(lambda user: user.is_authenticated and user.is_staff)
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('blog')
    else:
        form = BlogForm()

    return render(request, 'main/create_blog.html', {'form': form})


def videos(request):
    return render(request, 'main/videos.html')