
from django.urls import path
from .views import blog_view, blog_detail_view, blog_create_view, blog_update_view, blog_delete_view
from .views import speciality_detail_view,speciality_update_view,speciality_create_view,speciality_delete_view

urlpatterns = [
    path('blog/', blog_view, name='blog-list'),
    path('blog/<int:id>/', blog_detail_view, name='blog-detail'),
    path('blog/create/', blog_create_view, name='blog-create'),
    path('blog//<int:id>/update/', blog_update_view, name='blog-update'),
    path('blog//<int:id>/delete/', blog_delete_view, name='blog-delete'),
]
