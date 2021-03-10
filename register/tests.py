from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, course_title
from .models import Course_D

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

class CourseTitle(TestCase):
    def setUp(self):
        Course_D.objects.create(Course_Name='ทดสอบ', Course_ID='KMAAA02')

    def test_course_title_view_success_status_code(self):
        url = reverse('course_title', kwargs={'PK_Course_D': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_course_title_view_not_found_status_code(self):
        url = reverse('course_title', kwargs={'PK_Course_D': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_course_title_url_resolves_course_title_view(self):
        view = resolve('/regist/1/')
        self.assertEquals(view.func, course_title)



# Create your tests here.
