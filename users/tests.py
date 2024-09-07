from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

class UserModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com', password='password', role='client')
        self.profile = Profile.objects.create(user=self.user, biography='Test biography', contact='1234567890')

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, get_user_model()))
        self.assertEqual(self.user.__str__(), self.user.username)

    def test_profile_creation(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEqual(self.profile.__str__(), f"{self.user.username}'s profile")
