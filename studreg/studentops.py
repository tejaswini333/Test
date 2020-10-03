from abc import ABC,abstractmethod

class StudentService(ABC):

    @abstractmethod
    def add_new_student(self,stud):
        pass

    @abstractmethod
    def update_student_record(self,studId,stud):
        pass

    @abstractmethod
    def fetch_all_students(self):
        pass

    @abstractmethod
    def fetch_student_record(self,sid):
        pass

    @abstractmethod
    def delete_student_record(self,sid):
        pass


from studreg.models import Student

def valiate_email_field(email):
    if email and "com" in email.split("."):
        return True

from courseapp.models import Courses
#service --> database model -- ORM
class StudentServiceImpl(StudentService):


    def add_new_student(self, stud,courseIds):
        if type(stud)==Student:
            if valiate_email_field(stud.email):
                stud.save() # add -> insert ->
                 #this is to save-- only student info

                #assign courses to student
                for crid in courseIds:
                    stud.courserefs.add(Courses.objects.filter(id=crid).first())

                stud.save()

                return "Student<{}> Record Inserted ".format(stud.id)
            else:
                return "Invalid Email Address "
        return "Invalid Student Type.."

    def update_student_record(self, st,formdata):
        if valiate_email_field(formdata['semail']):
            st.email = formdata['semail']
            st.fname = formdata['sfnm']
            st.lname = formdata['slnm']
            st.courserefs.clear() # will remove all courses from student
            st.save() # record id alread present -- save-- update

            courseIds = [int(cid) for cid in formdata.getlist('crlist')]
            for crid in courseIds:
                st.courserefs.add(Courses.objects.filter(id=crid).first())
            st.save()


            return "Student<{}> Record Updated ".format(st.id)
        else:
            return "Invalid Email Address"


    def fetch_all_students(self):
        return Student.objects.filter(active='Y').all()

    def fetch_student_record(self, sid):
        return Student.objects.filter(active='Y',id=sid).first()

    def delete_student_record(self, sid):
        st = self.fetch_student_record(sid)
        if st:
            st.active='N'
            st.save()
            return "Student<{}> Record Deleted".format(sid)
        else:
            return "Student<{}> Record No Found So cannot delete".format(sid)

