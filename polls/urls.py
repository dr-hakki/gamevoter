from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('action', views.indexaction, name='indexaction'),
    path('fps', views.indexfps, name='indexfps'),
    path('moba', views.indexmoba, name='indexmoba'),
    path('racing', views.indexracing, name='indexracing'),
    path('rpg', views.indexrpg, name='indexrpg'),
    path('sports', views.indexsports, name='indexsports'),
    path('story', views.indexstory, name='indexstory'),
    path('simulation', views.indexsimulation, name='indexsimulation'),
    path('othergames', views.indexotherg, name='indexotherg'),
    path('strategy', views.indexstrategy, name='indexstrategy'),
    path('comparison', views.indexcomparison, name='indexcomparison'),
    path('series', views.indexseries, name='indexseries'),
    path('player', views.indexplayer, name='indexplayer'),
    path('team', views.indexteam, name='indexteam'),
    path('other', views.indexother, name='indexother'),
    path('popular', views.indexpopular, name='indexpopular'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('resultsdata/<str:obj>/', views.resultsData, name="resultsdata"),
]