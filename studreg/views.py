from django.shortcuts import render
from studreg.models import Student
from courseapp.models import Courses
#-----------------------Student Crud Operations-----------------
from studreg.studentops import StudentServiceImpl
simpl = StudentServiceImpl()
def create_edit_new_student(req):
    msg = ''
    dummyst = Student.get_empty_student()
    if req.method=='POST':
        formdata = req.POST  #formdata
        sid = int(formdata['sid']) #get id from formdata
        stud = simpl.fetch_student_record(sid) # service--> stud record
        if stud: #in case stud record present
            msg = simpl.update_student_record(stud,formdata)
            if "Email" in msg:
                dummyst = Student(fname=formdata['sfnm'],
                         lname=formdata['slnm'],
                         email=formdata['semail'],
                         dob=formdata['sdob'],
                         contact=formdata['smob'],
                         qual=formdata['squal'],
                         gender=formdata['sgen'])
                dummyst.id= sid
        else:
            courseIds = [int(cid) for cid in formdata.getlist('crlist')]

            print("COURSEIDs -- ",courseIds)
            st = Student(fname=formdata['sfnm'],
                         lname=formdata['slnm'],
                         email=formdata['semail'],
                         dob=formdata['sdob'],
                         contact=formdata['smob'],
                         qual=formdata['squal'],
                         gender=formdata['sgen'])
            msg = simpl.add_new_student(st,courseIds)
            if "Email" in msg:
                dummyst = st
                dummyst.id = sid
    return render(req, 'stud.html', {"resp": msg,
                                    "stud":dummyst,
                                     "crs" : Courses.objects.filter(active='Y'),
                                    "sts": simpl.fetch_all_students()})


def fetch_student_info(req,sid):
    return render(req, 'stud.html', {"stud": simpl.fetch_student_record(sid),
                                     "crs": Courses.objects.filter(active='Y'),
                                    "sts": simpl.fetch_all_students()})


def delete_student_info(req,sid):
    msg = simpl.delete_student_record(sid)
    return render(req, 'stud.html', {"resp": msg,
                                     "crs": Courses.objects.filter(active='Y'),
                                    "stud": Student.get_empty_student(),
                                    "sts": simpl.fetch_all_students()})
