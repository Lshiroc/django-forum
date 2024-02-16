from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>', views.detail, name='detail'),
    path('upvote/<int:pk>', views.upvote, name='upvote'),
    path('downvote/<int:pk>', views.downvote, name='downvote'),
]
