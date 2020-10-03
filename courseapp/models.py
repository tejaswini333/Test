from django.db import models
from studreg.models import Student,BaseModel

# Create your models here.
class Courses(BaseModel):
    name = models.CharField('cr_name', max_length=30)
    code = models.CharField('cr_code', max_length=30)
    fees = models.FloatField('cr_fee')
    duration = models.CharField('cr_duration', max_length=30)
    studrefs = models.ManyToManyField(Student,related_name='courserefs')

    @staticmethod
    def get_empty_course():
        return Courses(id=0,name='',code='',fees=0.0,duration='')

    class Meta: # this inner class--> represents additional about courses model--> metadata
        db_table = 'Courses_Info'
