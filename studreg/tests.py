from rest_framework.test import APITestCase
from rest_framework import status
from studreg.models import Student
from studreg.serializers import studentserializer
import json

# Create your tests here.
class Teststudentreg(APITestCase):

    def test_stud_registration(self):
        #data = {"fname":"Sanu","lname":"More","email":"sanu@gmail.com","dob":"04-02-1992",
           #     "contact":"9865412378","qual":"MCA","gender":"F"}
        response = self.client.post("student/register/")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)