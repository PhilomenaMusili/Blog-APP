from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_post, name='create'),
    path('', views.post_list, name='list'),
    path('detail/<int:id>/', views.post_detail, name='detail'),
    path('update/<int:id>/', views.update_post, name='update'),
    path('delete/<int:id>/', views.delete_post, name='delete'),
]