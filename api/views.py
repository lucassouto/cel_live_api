from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status
from .models import Course
from .serializers import CourseSerializer


@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)
