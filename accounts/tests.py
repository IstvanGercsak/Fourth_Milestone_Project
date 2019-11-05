from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class HomeTesCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_arrive_at_login_page(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_login(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

    def test_arrive_at_register_page(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    def test_arrive_at_profile_page(self):
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")

    # Ask the mentor about this
    def test_logout_page(self):
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        page = self.client.get("/accounts/logout/")
        self.assertRedirects(page, '/', status_code=302)
