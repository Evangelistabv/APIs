from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class Post(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Post