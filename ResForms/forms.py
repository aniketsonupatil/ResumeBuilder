
from crispy_forms.layout import Field,Layout,Submit,Row, Column,Button
from crispy_forms.bootstrap import FormActions,AppendedText
from django.core.validators import EMPTY_VALUES
from django.forms import ModelForm, widgets,Select,Textarea
from crispy_forms.helper import FormHelper
from ResBuild.models import *
from django.urls import reverse_lazy

# Create the form class.
class AchivementsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AchivementsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Field('AchivementName',placeholder='Enter Achivement',css_class='my-3'),
            Row(
            Field('AchivementPeriod',css_class='col my-3',placeholder='Enter Achivement Time Period'),
            Field('AchiveType',css_class='col my-3',help_text='Achivement Type'),
            #AppendedText('AchiveType','<i class="fa fa-angle-down fa-2x"></i>'),
            css_class='row-cols-md-2 row-cols-1 row'
            ),
            FormActions(
                Submit('submit', 'ADD',css_class='btn btn-success'),
                Button('cancel', 'Cancel',onclick="window.location.href = '{}';".format(reverse_lazy('resBuild:Index')))
            )  
        )
        #self.helper.form_show_labels = False
    class Meta:
        model = Achivements
        fields = '__all__'
        labels = {
            'AchivementName': 'What was your Achievement?',
            'AchivementPeriod': 'What the time period of your Achievement?',
            'AchiveType': 'What type of Achievement was this?'
        }
        help_texts={
            'AchivementName':'',
            'AchivementPeriod':'',
        }
        widgets={
            'AchiveType': Select(),     
        }
   

class CourseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Field('CourseName',placeholder='Course Name',css_class='my-3'),
            
            Field('CourseType',css_class='col my-3'),
            #AppendedText('AchiveType','<i class="fa fa-angle-down fa-2x"></i>'),
            
            FormActions(
                Submit('submit', 'ADD',css_class='btn btn-success'),
                Button('cancel', 'Cancel',onclick="window.location.href = '{}';".format(reverse_lazy('resBuild:Index')))
            )  
        )
        #self.helper.form_show_labels = False
    class Meta:
        model = Courses
        fields = '__all__'
        labels = {
            'CourseName': 'Name Of Course',
            'CourseType': 'What Type of Course',
            
        }
        help_texts={
            'CourseName':'',
        }
        widgets={
            'CourseType': Select(),     
        }


class ProjectForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Field('ProjectName',placeholder='Project Name',css_class='my-3'),
            Row(
            Field('Tag1',css_class='col my-3',placeholder='Left Tag'),
            Field('Tag2',css_class='col my-3',placeholder='Right Tag'),
            Field('ProjectPeriod',css_class='col my-3',placeholder='Time'),
            #AppendedText('AchiveType','<i class="fa fa-angle-down fa-2x"></i>'),
            css_class='row-cols-md-2 row-cols-lg-3 row'
            ),
            Field('ProjectDesc',placeholder='Project Description',css_class='my-3'),
            FormActions(
                Submit('submit', 'ADD',css_class='btn btn-success'),
                Button('cancel', 'Cancel',onclick="window.location.href = '{}';".format(reverse_lazy('resBuild:Index')))
            )  
        )
        #self.helper.form_show_labels = False
    class Meta:
        model = Projects
        fields = '__all__'
        labels = {
            'ProjectName': 'Name of Project',
            'Tag1': 'Left Tag',
            'Tag2': 'Right Tag',
            'ProjectPeriod': 'Duration/Period of Project',
            'ProjectDesc': 'Project Description'
        }
        help_texts={
            'ProjectName': '',
            'Tag1': '',
            'Tag2': '',
            'ProjectPeriod': '',
            'ProjectDesc': ''
        }
        widgets={
            'ProjectDesc': Textarea(attrs={"rows":5, "cols":10}),     
        }


class PorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Field('PorName',placeholder='POR Name',css_class='my-3'),
            Row(
            Field('Tag1',css_class='col my-3',placeholder='Enter Tag'),
            Field('PorPeriod',css_class='col my-3',placeholder='Time'),
            #AppendedText('AchiveType','<i class="fa fa-angle-down fa-2x"></i>'),
            css_class='row-cols-md-2 row-cols-lg-2 row'
            ),
            Field('PorDesc',placeholder='POR Description',css_class='my-3'),
            FormActions(
                Submit('submit', 'ADD',css_class='btn btn-success'),
                Button('cancel', 'Cancel',onclick="window.location.href = '{}';".format(reverse_lazy('resBuild:Index')))
            )  
        )
        #self.helper.form_show_labels = False
    class Meta:
        model = PORs
        fields = '__all__'
        labels = {
            'PorName': 'Name of POR',
            'Tag1': 'Enter Tag',
            'PorPeriod': 'Duration/Period of POR',
            'PorDesc': 'POR Description'
        }
        help_texts={
            'PorName': '',
            'Tag1': '',
            'PorPeriod': '',
            'PorDesc': ''
        }
        widgets={
            'PorDesc': Textarea(attrs={"rows":5, "cols":10}),     
        }
  
class SkillForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.layout = Layout(
            Field('SkillName',placeholder='Skill Name',css_class='my-3'),
            
            Field('SkillType',css_class='col my-3'),
            #AppendedText('AchiveType','<i class="fa fa-angle-down fa-2x"></i>'),
            
            FormActions(
                Submit('submit', 'ADD',css_class='btn btn-success'),
                Button('cancel', 'Cancel',onclick="window.location.href = '{}';".format(reverse_lazy('resBuild:Index')))
            )  
        )
        #self.helper.form_show_labels = False
    class Meta:
        model = Skills
        fields = '__all__'
        labels = {
            'SkillName': 'Enter Skill',
            'SkillType': 'Enter Skill Type',
            
        }
        help_texts={
            'SkillName':'',
        }
        widgets={
            'SkillType': Select(),     
        }


"""

'AchiveType': Select(attrs={
                'class':'col'
            } 


def __init__(self, data=None, files=None, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('query', placeholder='Search ...'),
        )

        or
def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper(self)
    self.helper.label_class = 'sr-only'
    self.helper.form_tag = False
    self.helper.layout = Layout()

    Field('field_name', css_class="black-fields")

"""  