from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from.models import Post


# Create your views here.

def postline(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'apps/postline.html', {'posts': posts})


def postdetail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'apps/postdetail.html', {'posts': posts})
