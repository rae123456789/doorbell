from django.urls import path

from . import views

app_name = 'doorbell'

urlpatterns = [
    path('home', views.index, name='home'),
    path('signin', views.signin, name='signin'),
    path('', views.load_signup_page, name='login'),
    path('logout', views.logout, name = 'logout'),
    path('signup', views.create_user, name='signup'),
    path('group/<str:group_name>', views.group, name = 'group'),
    path('group/<str:group_name>/post', views.post, name = 'post'),
    path('joingroup/<str:group_name>', views.joingroup, name = 'joingroup'),
    path('search_posts', views.search_posts, name = 'search_posts'),
    path('like/<int:post_id>', views.like,name = 'like' ),
    path('unlike/<int:post_id>', views.unlike,name = 'unlike' ),
    path('delete/<int:post_id>', views.delete,name = 'delete' ),
    path('polls', views.polls, name = 'polls'),
    path('join', views.join, name = 'join')


]


