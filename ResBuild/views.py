from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings

from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.contrib.auth import login
from django.contrib import messages

from django.forms.models import model_to_dict
from ResBuild.render import Render
from django.views import View
from django.urls import reverse_lazy
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterForm

class IndexView(View):
    def get(self,request):
        achievementids= request.session.get('achievementids',False)
        if (achievementids) : del(request.session['achievementids'])
        courseids= request.session.get('courseids',False)
        if (courseids) : del(request.session['courseids'])
        projectids= request.session.get('projectids',False)
        if (projectids) : del(request.session['projectids'])
        porids= request.session.get('porids',False)
        if (porids) : del(request.session['porids'])
        skillids= request.session.get('skillids',False)
        if (skillids) : del(request.session['skillids'])
        
        achievements = Achivements.objects.all();
        skilltypes=SkillTypes.objects.all();
        skills=Skills.objects.all();
        coursetypes=CourseTypes.objects.all();
        courses=Courses.objects.all();
        projects=Projects.objects.all();
        pors=PORs.objects.all();
        ctx={
            'achievements':achievements,
            'skilltypes':skilltypes,
            'skills':skills,
            'coursetypes':coursetypes,
            'courses':courses,
            'projects':projects,
            'pors':pors
        }
        return render(request,'ResBuild/HomePage.html',ctx)

    def post(self,request):
        achievementids = request.POST.getlist('achievementIDs')
        courseids = request.POST.getlist('courseIDs')
        projectids = request.POST.getlist('projectIDs')
        porids = request.POST.getlist('porIDs')
        skillids = request.POST.getlist('skillIDs')

        request.session['achievementids']=achievementids
        request.session['courseids']=courseids
        request.session['projectids']=projectids
        request.session['porids']=porids
        request.session['skillids']=skillids

        return redirect(reverse_lazy('resBuild:Genrated'))


class GenrateView(View):
    template_name='ResBuild/Genrated.html'
    def get(self,request):
        achievementids=request.session.get('achievementids',False)
        courseids=request.session.get('courseids',False)
        projectids=request.session.get('projectids',False)
        porids=request.session.get('porids',False)
        skillids=request.session.get('skillids',False)

        achievements=Achivements.objects.filter(pk__in= achievementids)
        courses=Courses.objects.filter(pk__in= courseids)
        projects=Projects.objects.filter(pk__in= projectids)
        pors=PORs.objects.filter(pk__in= porids)
        skills=Skills.objects.filter(pk__in= skillids)

        coursetypes=CourseTypes.objects.all();
        skilltypes=SkillTypes.objects.all();
        ctx={
            'achievements':achievements,
            'courses':courses,
            'projects':projects,
            'pors':pors,
            'skills':skills,
            'coursetypes':coursetypes,
            'skilltypes':skilltypes,
            
        }
        #return render(request,'ResBuild/Genrated.html',ctx)      
        template_string = render_to_string(self.template_name, ctx)
        html = HTML(string=template_string, base_url=request.build_absolute_uri())
        main_doc = html.render()
        pdf = main_doc.write_pdf()
        
        response = HttpResponse(pdf, content_type='application/pdf')
        #Download as attachment
        # response['Content-Disposition'] = 'attachment; filename=packslip-{0}.pdf'.format(packslip_id)
        # Display in browser
        response['Content-Disposition'] = 'filename=GenratedTest.pdf'
        return response

class GenTestView(LoginRequiredMixin,View):
    def get(self,request):
        achievements = Achivements.objects.all();
        skilltypes=SkillTypes.objects.all();
        skills=Skills.objects.all();
        coursetypes=CourseTypes.objects.all();
        courses=Courses.objects.all();
        projects=Projects.objects.all();
        pors=PORs.objects.all();
        ctx={
            'achievements':achievements,
            'skilltypes':skilltypes,
            'skills':skills,
            'coursetypes':coursetypes,
            'courses':courses,
            'projects':projects,
            'pors':pors
        }
        return render(request,'ResBuild/GenTest.html',ctx)


class Register(View):
    def get(self,request):
        form = RegisterForm()
        ctx = {'form':form}
        return render(request,"registration/registration.html",ctx)
    
    def post(self,request):
        form = RegisterForm(request.POST)
        if not form.is_valid():
            ctx={'form':form}
            return render(request,"registration/registration.html",ctx)

        user = form.save()
        login(request,user)
        return redirect('resBuild:GenTest')


        
"""
class TestView(View):
    def get(self,request):
        data= request.session.get('data',False)
        if (data) : del(request.session['data'])
        achievements=Achivements.objects.all();
        ctx={
            'achievements': achievements,
        }
        return render(request,'ResBuild/test1.html',ctx)
    
    def post(self,request):
        achievementids = request.POST.getlist('achievementIDs')
        #achievements=Achivements.objects.filter(pk__in= achievementids)
        # ctx={
        #     'achievements':achievements,
        #     'achievementids':achievementids,
        # }
        #data=json.loads(json.dumps(ctx, default=lambda o: o.__dict__))
        #data = serializers.serialize('json', ctx)
        request.session['data']=achievementids
        return redirect(reverse_lazy('resBuild:Test2'))
        # for item in ctx:
        #     item['achievements'] = model_to_dict(item['achievements'])
        # return HttpResponse(json.simplejson.dumps(ctx), mimetype="application/json")
        
class TestView2(View):
    template_name='ResBuild/test2.html'
    def get(self,request):
        data=request.session.get('data',False)
        achievements=Achivements.objects.filter(pk__in= data)

        ctx={
            'achievements':achievements,
        }        
        template_string = render_to_string(self.template_name, ctx)
        html = HTML(string=template_string, base_url=request.build_absolute_uri())
        main_doc = html.render()
        pdf = main_doc.write_pdf()
        
        response = HttpResponse(pdf, content_type='application/pdf')
        #Download as attachment
        # response['Content-Disposition'] = 'attachment; filename=packslip-{0}.pdf'.format(packslip_id)
        # Display in browser
        response['Content-Disposition'] = 'filename=Testing.pdf'
        return response


class TestView2(View):
    def get(self,request):
        data=request.session.get('data',False)
        achievements=Achivements.objects.filter(pk__in= data)

        ctx={
            'achievements':achievements,
            'request': request
            #'achievementids':achievementids,
        }
        #pdf = render_to_pdf('ResBuild/test2.html',ctx)
        #return HttpResponse(pdf, content_type='application/pdf')
        pdf = Render.render('ResBuild/test2.html', ctx)
        return HttpResponse(pdf, content_type='application/pdf')
        # if pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     filename = "Test_%s.pdf" %("ing")
        #     content = "inline; filename='%s'" %(filename)
        #     download = request.GET.get("download")
        #     if download:
        #         content = "attachment; filename='%s'" %(filename)
        #     response['Content-Disposition'] = content
        #     return response
        # return HttpResponse("Not found")

class TestView(View):
    def get(self,request):
        data= request.session.get('data',False)
        if (data) : del(request.session['data'])
        achievements=Achivements.objects.all();
        ctx={
            'achievements': achievements,
        }
        return render(request,'ResBuild/test1.html',ctx)
    
    def post(self,request):
        achievementids = request.POST.getlist('achievementIDs')
        #achievements=Achivements.objects.filter(pk__in= achievementids)
        # ctx={
        #     'achievements':achievements,
        #     'achievementids':achievementids,
        # }
        #data=json.loads(json.dumps(ctx, default=lambda o: o.__dict__))
        #data = serializers.serialize('json', ctx)
        request.session['data']=achievementids
        return redirect(reverse_lazy('resBuild:Test2'))
        # for item in ctx:
        #     item['achievements'] = model_to_dict(item['achievements'])
        # return HttpResponse(json.simplejson.dumps(ctx), mimetype="application/json")


class TestView2(View):
    def get(self,request):
        data=request.session.get('data',False)
        achievements=Achivements.objects.filter(pk__in= data)

        ctx={
            'achievements':achievements,
            #'achievementids':achievementids,
        }
        return render(request,'ResBuild/test2.html',ctx)


class TestView(View):
    def get(self,request):
        achievements=Achivements.objects.all();
        ctx={
            'achievements': achievements,
        }
        return render(request,'ResBuild/test1.html',ctx)
    
    def post(self,request):
        achievementids = request.POST.getlist('achievementIDs')
        achievements=Achivements.objects.filter(pk__in= achievementids)

        ctx={
            'achievements':achievements,
            #'achievementids':achievementids,
        }
        return render(request,'ResBuild/test2.html',ctx)


def post(self,request):
        achievements = request.POST
        #achievements=Achivements.objects.filter(pk__in= achievementids)

        ctx={
            'achievements':achievements,
            #'achievementids':achievementids,
        }
        return render(request,'ResBuild/test2.html',ctx)



    def get(self,request):
        pors=PORs.objects.all();
        ctx={'pors':pors}
        return render(request,'ResBuild/pors.html',ctx)
"""