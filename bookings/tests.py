from django.test import TestCase
from .models import Booking
from services.models import Service
from therapists.models import Therapist
from users.models import User

class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.service = Service.objects.create(name='Test Service', description='Test Description', price=100.00, duration='01:00:00', category='Test Category')
        self.therapist = Therapist.objects.create(profile=self.user.profile, qualification='Test Qualification', experience=5)
        self.booking = Booking.objects.create(user=self.user, service=self.service, therapist=self.therapist, date='2023-01-01', time='10:00:00', status='confirmed')

    def test_booking_creation(self):
        self.assertTrue(isinstance(self.booking, Booking))
        self.assertEqual(self.booking.__str__(), f"Booking {self.booking.id} by {self.user.username}")
