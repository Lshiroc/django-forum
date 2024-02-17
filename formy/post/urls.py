from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('<int:pk>', views.detail, name='detail'),
    path('upvote/<int:pk>', views.upvote_post, name='upvote_post'),
    path('downvote/<int:pk>', views.downvote_post, name='downvote_post'),
    path('upvote/comment/<int:postid>/<int:commentid>/', views.upvote_comment, name='upvote_comment'),
    path('downvote/comment/<int:postid>/<int:commentid>/', views.downvote_comment, name='downvote_comment'),

]
