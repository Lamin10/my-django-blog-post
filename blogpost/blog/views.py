from django.shortcuts import render
from .models import BlogPost


# Create your views here.

def index(request):
    # Fetch latest blog posts from the database
    latest_posts = BlogPost.objects.all().order_by('-publication_date')[:5]

    # Render the homepage template with the latest posts
    return render(request, 'index.html', {'latest_posts': latest_posts})

