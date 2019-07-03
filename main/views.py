from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'khadija',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'August 28, 2019'
    }
]



# Create your views here.
def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request=request,
                  template_name='main/blog.html',
                  context=context)



def about(request):
    return render(request=request,
                  template_name='main/about.html')