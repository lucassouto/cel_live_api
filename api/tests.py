from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Course


class TestViews(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(
            title='Curso de Python',
            tutor='Lucas Souto',
            number_lessons=25,
            workload=5.5
        )

    def test_get_courses(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_courses(self):
        response = self.client.post(reverse('course_list'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
