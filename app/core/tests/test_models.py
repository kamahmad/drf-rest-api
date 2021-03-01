from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):


    def test_create_user_with_email(self):
        """Test if new user is created with an email address"""
        email = 'abc@abc.com'
        password = 'test123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test if the email is normalised"""
        email = "abc@ABC.cOM"
        user = get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test if the email entered is valid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_superuser(self):
        """Test if new superuser is created"""
        user = get_user_model().objects.create_superuser(
            'abc@abc.com',
            'test123'
            )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
