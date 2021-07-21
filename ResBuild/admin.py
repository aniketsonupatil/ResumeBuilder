from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(AchivementTypes)
admin.site.register(Achivements)
admin.site.register(Projects)
admin.site.register(PORs)
admin.site.register(CourseTypes)
admin.site.register(Courses)
admin.site.register(SkillTypes)
admin.site.register(Skills)