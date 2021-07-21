from django.urls import path

from . import views
app_name ='resBuild'
urlpatterns = [
    path('',views.IndexView.as_view(),name='Index'),
    path('gentest',views.GenTestView.as_view(),name='GenTest'),
    path('register', views.Register.as_view(), name='Register'),
    path('genratedresume',views.GenrateView.as_view(),name='Genrated'),
    #path('test',views.TestView.as_view(),name='Test'),
    #path('test2',views.TestView2.as_view(),name='Test2'),
    #path('achievements', views.AchievementView.as_view(), name='achievements'),
    #path('skills',views.SkillsView.as_view(),name='skills'),
    #path('courses',views.coursesView.as_view(),name='courses'),
    #path('projects',views.projecstView.as_view(),name='prjects'),
    #path('pors',views.porsView.as_view(),name='pors'),
]