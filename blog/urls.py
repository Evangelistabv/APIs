from django.urls import path
from .views import Post

urlpatterns = [
    path('post/', Post.as_view(), name='post-create'),
]