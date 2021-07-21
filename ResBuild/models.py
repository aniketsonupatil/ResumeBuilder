from django.db import models
from django.db.models.base import Model
from django.core.validators import MinLengthValidator


# Create your models here.
class AchivementTypes(models.Model):
    Type_Achive= models.CharField(
         max_length=200,
        help_text='Enter Achivement Type',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.Type_Achive
class Achivements(models.Model):
    AchivementName=models.CharField(
         max_length=200,
        help_text='Enter Achivement',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    AchivementPeriod=models.CharField(
         max_length=200,
        help_text='Enter Achivement Time Period',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    AchiveType=models.ForeignKey('AchivementTypes', on_delete=models.CASCADE, null=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.AchivementName

class Projects(models.Model):
    ProjectName=models.CharField(
         max_length=200,
        help_text='Enter Prject Name',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    Tag1=models.CharField(
         max_length=200,
        help_text='Enter Tag 1',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    Tag2=models.CharField(
         max_length=200,
        help_text='Enter Tag 2',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    ProjectPeriod=models.CharField(
         max_length=200,
        help_text='Enter Project Time Period',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    ProjectDesc=models.CharField(
         max_length=200,
        help_text='Enter Project Description',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    def __str__(self):
        """String for representing the Model object."""
        return self.ProjectName

class PORs(models.Model):
    PorName=models.CharField(
         max_length=200,
        help_text='Enter POR Name',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    Tag1=models.CharField(
         max_length=200,
        help_text='Enter Tag 1',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    PorPeriod=models.CharField(
         max_length=200,
        help_text='Enter Project Time Period',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    PorDesc=models.CharField(
         max_length=200,
        help_text='Enter POR Description',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    def __str__(self):
        """String for representing the Model object."""
        return self.PorName


class CourseTypes(models.Model):
    CourseType=models.CharField(
         max_length=200,
        help_text='Enter Course Type',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    def __str__(self):
        """String for representing the Model object."""
        return self.CourseType

class Courses(models.Model):
    CourseName=models.CharField(
         max_length=200,
        help_text='Enter Course Name',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    CourseType=models.ForeignKey('CourseTypes', on_delete=models.CASCADE, null=False)
    def __str__(self):
        """String for representing the Model object."""
        return self.CourseName


class SkillTypes(models.Model):
    SkillType=models.CharField(
         max_length=200,
        help_text='Enter Course Type',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    def __str__(self):
        """String for representing the Model object."""
        return self.SkillType

class Skills(models.Model):
    SkillName=models.CharField(
         max_length=200,
        help_text='Enter Course Name',
        validators=[MinLengthValidator(2, "Make must be greater than 1 character")]
    )
    SkillType=models.ForeignKey('SkillTypes', on_delete=models.CASCADE, null=False)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.SkillName
