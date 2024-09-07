from django.test import TestCase
from .models import Service

class ServiceModelTest(TestCase):

    def setUp(self):
        self.service = Service.objects.create(
            name='Test Service',
            description='Test Description',
            price=100.00,
            duration='01:00:00',
            category='Test Category'
        )

    def test_service_creation(self):
        self.assertTrue(isinstance(self.service, Service))
        self.assertEqual(self.service.__str__(), self.service.name)
