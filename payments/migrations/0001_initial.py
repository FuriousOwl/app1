# Generated by Django 4.2.7 on 2024-05-22 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('method', models.CharField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer')], max_length=20)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookings.booking')),
            ],
        ),
    ]