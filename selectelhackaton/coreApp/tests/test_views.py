from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.conf import settings
import                  importlib


from selectelhackaton.auth.models import User, UserProfile

class ViewsTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Установки запускаются перед запуском теста на уровне настройки всего класса"""
        user = User.objects.create(email="root@test.com", password='top_secret')
        user.save()

    def setUp(self): 
        """Установки запускаются перед каждым тестом."""
        user = User.objects.create(email="user@test.com", password='top_secret')
        user.save()
        self.client = Client()
        

    def tearDown(self):
        """Очистка после каждого метода"""
        pass

    # TESTS: 
    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        
        self.assertEqual(1 + 1, 2)
