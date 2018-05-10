from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status


@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        return Response(status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)
