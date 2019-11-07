from django.db import models

# Create your models here.
from django.contrib.auth.models import User, BaseUserManager
from django.utils.crypto import get_random_string


class UsersManager(BaseUserManager):
    def create_administrator(self, username, first_name, last_name):
        customer = Customer(username=username,
                            first_name=first_name, last_name=last_name)
        password = get_random_string(length=6)
        customer.set_password(password)
        customer.is_staff = True
        customer.save()
        return customer


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def upload_products(self):
        pass
    #  csv_file = request.FILES["csv_file"]
    #   semester = request.data['semester']
    #    if not csv_file.name.endswith(".csv"):
    #         return HttpResponse(status=HTTP_400_BAD_REQUEST)
    #     file_data = csv_file.read().decode("utf-8")
    #     lines = file_data.split("\n")
    #     response = "Revisar filas:\n"
    #     i = 0
    #     for line in lines:
    #         j = 0
    #         if (line):
    #             fields = line.split(",")
    #             object_student = {
    #                 "user_id": fields[0], "username": fields[3], "first_name": fields[1], "last_name": fields[2],  "password": 'ninguna'}
    #             json_student = json.dumps(object_student)
    #             json_student = json.loads(json_student)
    #             serializer = self.serializer_student(data=json_student)
    #             if (serializer.is_valid(raise_exception=False)):
    #                 serializer.save()
    #             else:
    #                 response = response + \
    #                     "\t " + str(i + 1) + "\n"
    #                 j = i
    #             # FIND STUDENT

    #             student = Student.objects.get(
    #                 user_id=json_student.get('user_id')).id
    #             print(i)
    #             # - - - - -
    #             # FIND COURSE
    #             course_obj = CourseDetail.objects.filter(
    #                 course__course_id=fields[4], semester=semester)

    #             if (course_obj):
    #                 course = course_obj.first().id

    #             # - - - - -
    #             object_enrrollment = {"student": student, "course": course}
    #             json_enrrollment = json.dumps(object_enrrollment)
    #             json_enrrollment = json.loads(json_enrrollment)
    #             serializer = self.serializer_enrrollment(data=json_enrrollment)
    #             print(serializer.is_valid())
    #             if (serializer.is_valid(raise_exception=False)):
    #                 serializer.save()
    #             else:
    #                 if j != i:
    #                     response = response + "\tcurso " + str(i + 1) + "\n"
    #             i = i + 1
