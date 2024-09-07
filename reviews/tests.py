from django.test import TestCase
from .models import Review
from users.models import User
from therapists.models import Therapist
from services.models import Service

class ReviewModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com', password='password', role='client')
        self.therapist = Therapist.objects.create(profile=self.user.profile, qualification='Test Qualification', experience=5)
        self.service = Service.objects.create(name='Test Service', description='Test Description', price=100.00, duration='01:00:00', category='Test Category')
        self.review = Review.objects.create(user=self.user, therapist=self.therapist, service=self.service, rating=5, comment='Great service!')

    def test_review_creation(self):
        self.assertTrue(isinstance(self.review, Review))
        self.assertEqual(self.review.__str__(), f"Review {self.review.id} by {self.user.username}")
