from django.shortcuts import render
from courseapp.models import Courses

def create_edit_new_course(req):
    msg = ''
    if req.method == 'POST':
        formdata = req.POST
        print('inside post method--',formdata)
        cr =  Courses.objects.filter(id=int(formdata['crid'])).first()
        if cr:
            cr.name = formdata['crname']
            cr.fees = formdata['crfees']
            cr.code = formdata['crcode']
            msg = "Course Record Updated"
        else:
            msg = "New Course Added..."
            cr = Courses(id=formdata['crid'],
                name=formdata['crname'],
                fees=formdata['crfees'],
                code=formdata['crcode'],
                duration=formdata['crdur'])
        cr.save()
    return render(req,'course.html',{"resp":msg,
                                     "cr" : Courses.get_empty_course(),
                                     "crlist": Courses.objects.filter(active='Y')})

#once user clicks on edit--> want to papulate values inside form
def fetch_course_info(req,crid):
    return render(req, 'course.html', {
                                       "cr": Courses.objects.get(id=crid),
                                       "crlist": Courses.objects.filter(active='Y')})


# once user clicks on delete --> want soft delete course record
def delete_course_info(req,crid):
    dbcr = Courses.objects.get(id=crid)
    msg = ''
    if dbcr:
        dbcr.active='N'
        dbcr.save()
        msg = 'Course deleted...!'
    return render(req, 'course.html', {"resp": msg,
                                       "cr": Courses.get_empty_course(),
                                       "crlist": Courses.objects.filter(active='Y')})



