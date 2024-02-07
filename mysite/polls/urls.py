from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.home, name = 'home'),    
    path('question/<int:question_id>', views.detail, name='detail'),    
    path('<int:question_id>/result', views.results, name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('practice', views.practice, name = 'practice'),
    path('create_poll', views.create_poll, name = 'create_poll'),


]



