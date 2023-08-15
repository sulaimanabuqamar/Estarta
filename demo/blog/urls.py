from django.urls import path
from .views import blog_list, blog_detail, blog_delete

urlpatterns = [
    path('posts/', blog_list, name="blog_list"),
    path('posts/<int:post_id>/', blog_detail, name="blog_detail"),
    path('posts/<int:post_id>/delete', blog_delete , name="blog_detail"),
]
