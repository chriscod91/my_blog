from django.urls import path
from .views import (
    BlogListView, 
    BlogDetailView, 
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    )
from django.views.generic import TemplateView

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("posts/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("posts/new/", BlogCreateView.as_view(), name="post_new"),
    path("posts/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("posts/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("logout/", TemplateView.as_view(template_name="registration/logout.html"), name="logout2"),
]