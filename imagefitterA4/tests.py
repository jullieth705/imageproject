from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from .views import fit_image

TEST_FILENAME = 'prueba.jpeg'
LOGIN_URL = '/accounts/login/'

class SecurityAccessViewsTestCase(TestCase):
	def test_login_loads_properly(self):
		response = self.client.get(LOGIN_URL)
		self.assertEqual(response.status_code, 200)

	def test_register_loads_properly(self):
		response = self.client.get('/accounts/register/')
		self.assertEqual(response.status_code, 200)

	def test_logout_without_login_redirect(self):
		response = self.client.get('/accounts/logout/')
		self.assertRedirects(response, LOGIN_URL, status_code=302, 
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

class ViewTestCase(TestCase):
	def setUp(self):
		self.credentials = {
			'username': 'testuser',
			'password': 'secret',
			'email':'testuser@test.com'}
		
		self.credentials_new_user = {
			'csrfmiddlewaretoken': ['RbRcj8j9GuIktQLK8Qdt5HHZqh24CqjJfpiYoNwKJyaXuJY0VYl5KBeYfe7ZK56H'], 
			'username': ['testuser2'], 
			'email': ['testuser2@gmail.com'], 
			'password1': ['secret'], 
			'password2': ['secret']}

		User.objects.create_user(**self.credentials)

	def get_valid_file(self):
		return settings.MEDIA_ROOT + '/'+settings.IMAGE_URL + TEST_FILENAME
	
	def test_login_succesful(self):
		response = self.client.post(LOGIN_URL, self.credentials, follow=True)
		self.assertTrue(response.context['user'].is_authenticated)

	
	def test_fit_image_succesful(self):
		correct_result = {	'path': settings.IMAGE_URL + TEST_FILENAME,
							'orientation': 'horizontal',
							'dimensions':  '797X796',
							'name': 'prueba'}
		source = SimpleUploadedFile(TEST_FILENAME, open(self.get_valid_file(), 'rb').read())
		source.content_type = 'image/jpeg'
		name = 'prueba'
		number_file = 0
		result = fit_image(source, name, number_file)
		self.assertEqual(result, correct_result)

	def test_register_successful(self):
		response = self.client.post('/accounts/register/', data=self.credentials_new_user, follow=True)
		self.assertEqual(response.status_code, 200)
		users = User.objects.all()
		self.assertEqual(users.count(), 1)

	