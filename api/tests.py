from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Course


class TestCourses(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.course = Course.objects.create(
            title='Curso de Django',
            tutor='Lucas Souto',
            number_lessons=15,
            workload=3
        )

    def test_get_courses(self):
        response = self.client.get(reverse('course_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_courses(self):
        response = self.client.post(
            reverse('course_list'),
            {
                'title': 'Curso de Python',
                'tutor': 'Guido van Rossum',
                'number_lessons': 25,
                'workload': 5.5
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail_courses(self):
        response = self.client.get(
            reverse('course_detail', kwargs={'pk': self.course.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_courses(self):
        response = self.client.put(
            reverse('course_detail', kwargs={'pk': self.course.id}),
            {
                'title': 'Curso de PHP',
                'tutor': 'Nanderson',
                'number_lessons': 50,
                'workload': 10
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_courses(self):
        response = self.client.delete(
            reverse('course_detail', kwargs={'pk': self.course.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
