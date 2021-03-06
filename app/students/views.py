from rest_framework.views import APIView
from rest_framework.response import Response

from .models import StudentModel
from .serializer import StudentSerializer


class AllStudent(APIView):

    def get(self, request):

        student = StudentModel.objects.all()
        student_serializer = StudentSerializer(student, many=True)
        return Response(student_serializer.data)

class AddStudent(APIView):

    def post(self, request):

        data = {

            'name': request.data.get('name'),
            'age': request.data.get('age')

        }

        student_serializer = StudentSerializer(data=data)

        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response(student_serializer.errors)

class SpecificStudent(APIView):

    def get_student(self, id):

        try:
            return StudentModel.objects.get(id=id)
        except StudentModel.DoesNotExist:
            return Response('Does not exist!')

    def get(self, request, id):

        student = self.get_student(id=id)
        student_serializer = StudentSerializer(student)
        return Response(student_serializer.data)
    
    def delete(self, request, id):

        student = self.get_student(id=id)
        student.delete()
        return Response('Deleted with sucessful!')

    def put(self, request, id):

        student = self.get_student(id=id)
        student_serializer = StudentSerializer(student, data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data)
        else:
            return Response('Try again, baby!')