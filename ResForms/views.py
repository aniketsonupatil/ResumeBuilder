from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from ResBuild.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ResForms.forms import *
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class AchievementMake(CreateView):
    form_class=AchivementsForm
    model=Achivements
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Enter Achievement Details"
        return context
class AchievementUpdate(UpdateView):
    form_class=AchivementsForm
    model=Achivements
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Achievement Details"
        return context
class AchievementDelete(DeleteView):
    #form_class=AchivementsForm
    model=Achivements
    fields = '__all__'
    template_name='ResForms/delete_confirm.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Achievement"
        
        return context

class CourseMake(CreateView):
    form_class=CourseForm
    model=Courses
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Enter Course Details"
        return context
class CourseUpdate(UpdateView):
    form_class=CourseForm
    model=Courses
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Course Details"
        return context
class CourseDelete(DeleteView):
    #form_class=CourseForm
    model=Courses
    fields = '__all__'
    template_name='ResForms/delete_confirm.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Course"
        
        return context


class ProjectMake(CreateView):
    form_class=ProjectForm
    model=Projects
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Enter Project Details"
        return context
class ProjectUpdate(UpdateView):
    form_class=ProjectForm
    model=Projects
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Project Details"
        return context
class ProjectDelete(DeleteView):
    #form_class=ProjectForm
    model=Projects
    fields = '__all__'
    template_name='ResForms/delete_confirm.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Project"
        
        return context


class PorMake(CreateView):
    form_class=PorForm
    model=PORs
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Enter POR Details"
        return context
class PorUpdate(UpdateView):
    form_class=PorForm
    model=PORs
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit POR Details"
        return context
class PorDelete(DeleteView):
    #form_class=PorForm
    model=PORs
    fields = '__all__'
    template_name='ResForms/delete_confirm.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete POR"
        
        return context


class SkillMake(CreateView):
    form_class=SkillForm
    model=Skills
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Enter Skill Details"
        return context
class SkillUpdate(UpdateView):
    form_class=SkillForm
    model=Skills
    template_name='ResForms/form_template.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Skill Details"
        return context
class SkillDelete(DeleteView):
    #form_class=SkillForm
    model=Skills
    fields = '__all__'
    template_name='ResForms/delete_confirm.html'
    success_url=reverse_lazy('resBuild:Index')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete Skill"
        
        return context
