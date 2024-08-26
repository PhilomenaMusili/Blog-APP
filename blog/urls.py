from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.post_list, name='list'),
    path('detail/<int:id>/', views.post_detail, name='detail'),
    
]