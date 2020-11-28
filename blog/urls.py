from django.urls import path
import mainApp.views
from .views import BlogView, BlogPostView, AddBlogPostView, EditPostView, DeletePostView

app_name = "blog"

urlpatterns = [
    path('', BlogView.as_view(), name="blog"),
    path('blog/', BlogView.as_view(), name="blog"),
    path('article/<int:pk>', BlogPostView.as_view(), name="article-detail"),
    path('addPost/', AddBlogPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
]