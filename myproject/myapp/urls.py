from django.urls import path
from .import views


urlpatterns = [
    path('', views.postline, name='postline'),
    path('post/<int:pk>/', views.postdetail, name='postdetail'),
]
