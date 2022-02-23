from .models import Post
from django.shortcuts import redirect, render, get_object_or_404

def post(request):
    lates_post = Post.objects.all().order_by("-id")[:4]
    return( {'latest_posts':lates_post})