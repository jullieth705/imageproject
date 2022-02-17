from django.test import TestCase
from django.contrib.auth.models import User


class AccessTestCase(TestCase):
	def test_login_loads_properly(self):
		response = self.client.get('/accounts/login/')
		self.assertEqual(response.status_code, 200)

	def test_register_loads_properly(self):
		response = self.client.get('/accounts/register/')
		self.assertEqual(response.status_code, 200)

	def test_logout_without_login_redirect(self):
		response = self.client.get('/accounts/logout/')
		self.assertRedirects(response, '/accounts/login/', status_code=302, 
							target_status_code=200, fetch_redirect_response=True)

	def test_home_without_login_redirect(self):
		response = self.client.get('/')
		self.assertRedirects(response, '/accounts/login/?next=/', status_code=302, 
							target_status_code=200, fetch_redirect_response=True)

	def test_galery_without_login_redirect(self):
		response = self.client.get('/galery')
		self.assertRedirects(response, '/accounts/login/?next=/galery', status_code=302, 
							target_status_code=200, fetch_redirect_response=True)

	def test_upload_without_login_redirect(self):
		response = self.client.get('/upload')
		self.assertRedirects(response, '/accounts/login/?next=/upload', status_code=302, 
							target_status_code=200, fetch_redirect_response=True)

class LoginTest(TestCase):
	def setUp(self):
		self.credentials = {
			'username': 'testuser',
			'password': 'secret',
			'email':'testuser@test.com'}
		User.objects.create_user(**self.credentials)
	
	def test_login(self):
		response = self.client.post('/accounts/login/', self.credentials, follow=True)
		self.assertTrue(response.context['user'].is_authenticated)
        								


