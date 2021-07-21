from django.urls import path

from . import views
app_name ='resForms'
urlpatterns = [
    path('achievement',views.AchievementMake.as_view(),name='AchievementMake'),
    path('achievement/<int:pk>/update/',views.AchievementUpdate.as_view(),name='AchievementUpdate'),
    path('achievement/<int:pk>/delete/',views.AchievementDelete.as_view(),name='AchievementDelete'),

    path('course',views.CourseMake.as_view(),name='CourseMake'),
    path('course/<int:pk>/update/',views.CourseUpdate.as_view(),name='CourseUpdate'),
    path('course/<int:pk>/delete/',views.CourseDelete.as_view(),name='CourseDelete'),

    path('project',views.ProjectMake.as_view(),name='ProjectMake'),
    path('project/<int:pk>/update/',views.ProjectUpdate.as_view(),name='ProjectUpdate'),
    path('project/<int:pk>/delete/',views.ProjectDelete.as_view(),name='ProjectDelete'),

    path('por',views.PorMake.as_view(),name='PorMake'),
    path('por/<int:pk>/update/',views.PorUpdate.as_view(),name='PorUpdate'),
    path('por/<int:pk>/delete/',views.PorDelete.as_view(),name='PorDelete'),

    path('skill',views.SkillMake.as_view(),name='SkillMake'),
    path('skill/<int:pk>/update/',views.SkillUpdate.as_view(),name='SkillUpdate'),
    path('skill/<int:pk>/delete/',views.SkillDelete.as_view(),name='SkillDelete'),


]