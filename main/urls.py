from django.urls import path
from .views import index, resources, pool, about, register
from .views import blog, blogpost, create_blog, videos

urlpatterns = [
    path('', index, name='home'),
    path('resources/', resources, name='resources'),
    path('pool/', pool, name='pool'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),
    path('blog/', blog, name='blog'),
    path('blog/<int:parameter>/', blogpost, name='blogpost'),
    path('blog/create/', create_blog, name='create_blog'),
    path('videos/', videos, name='videos'),
]