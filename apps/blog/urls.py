from django.urls import path
from .views import BlogView,CreateBlogView, DeleteBlogView,UpdateBlogView

urlpatterns = [
    path("blog/list",BlogView.as_view(),name="blog"),
    path("blog/create",CreateBlogView.as_view(),name="create_blog"),
    path("blog/update/<int:pk>/",UpdateBlogView.as_view(),name="update_blog"),
    path("blog/delete/<int:pk>/",DeleteBlogView.as_view(),name="delete_blog"),
]
