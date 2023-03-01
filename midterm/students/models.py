from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_leight=255, null=None, default=None)
    surname = models.CharField(max_leight=255, null=None, default=None)
    year_of_study = models.IntegerField(max_value=None, min_value=None)


    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return 'Name: {}, Surname: {}, Year of study: {}'.format(self.name, self.surname, self.year_of_study)
    
