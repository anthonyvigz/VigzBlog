from django.shortcuts import render

posts = [
    {
        'author': 'AnthonyV',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 7, 2020'
    },
    {
        'author': 'JaneD',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 8, 2020'
    }
]

# Create your views here.

def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})