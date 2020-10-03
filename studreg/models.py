from django.db import models

# Create your models here.

class BaseModel(models.Model):
    active = models.CharField('active', max_length=30,default='Y')
    created = models.DateTimeField('created_date',auto_now_add=True)
    updated = models.DateTimeField('modified_date',auto_now=True)

    class Meta:
        abstract = True


class Student(BaseModel):
    fname = models.CharField('stud_fname',max_length=30)
    lname = models.CharField('stud_lname', max_length=30)
    email = models.EmailField('stud_email')
    dob = models.CharField('stud_dob', max_length=30)
    contact = models.BigIntegerField('stud_mob')
    qual = models.CharField('stud_qual', max_length=30)
    gender =models.CharField('stud_gen', max_length=30)

#st = Student(fname,lname,email,dob,contact,qual,gender)

    @staticmethod
    def get_empty_student():
        return Student(id=0,fname='',lname='',email='',dob='',qual='',contact=0,gender='')

    class Meta:
        db_table = 'Stud_Info'


#Courses(id,name,fees,code,duration)