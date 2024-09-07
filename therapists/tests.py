from django.test import TestCase
from .models import Therapist
from users.models import User, Profile

class TherapistModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345')
        self.profile = Profile.objects.create(user=self.user, biography='Test Bio', contact='1234567890')
        self.therapist = Therapist.objects.create(profile=self.profile, qualification='Test Qualification', experience=5)

    def test_therapist_creation(self):
        self.assertTrue(isinstance(self.therapist, Therapist))
        self.assertEqual(self.therapist.__str__(), self.profile.user.username)
