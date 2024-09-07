from django.test import TestCase
from .models import Payment
from bookings.models import Booking

class PaymentModelTest(TestCase):

    def setUp(self):
        self.booking = Booking.objects.create(user_id=1, service_id=1, date='2023-01-01', time='10:00:00', status='confirmed')
        self.payment = Payment.objects.create(booking=self.booking, amount=100.00, method='credit_card')

    def test_payment_creation(self):
        self.assertTrue(isinstance(self.payment, Payment))
        self.assertEqual(self.payment.__str__(), f"Payment {self.payment.id} for booking {self.booking.id}")
