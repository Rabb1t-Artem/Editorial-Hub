from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from news.models import Newspaper, Topic
import os

class NewsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@test.com',
            years_of_experience=1
        )
        self.topic = Topic.objects.create(name='Test Topic')
        
        # Створюємо реальне тестове зображення
        image_path = os.path.join('media', 'news_images', 'culture.jpeg')
        with open(image_path, 'rb') as img:
            self.newspaper = Newspaper.objects.create(
                title='Test News',
                description='Test Description',
                redactor=self.user,
                image=SimpleUploadedFile(
                    name='culture.jpeg',
                    content=img.read(),
                    content_type='image/jpeg'
                )
            )
        self.newspaper.topics.add(self.topic)

    def test_index_view(self):
        response = self.client.get(reverse('news:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/index.html')

    def test_user_news_list_view_unauthorized(self):
        response = self.client.get(reverse('news:my_news'))
        self.assertEqual(response.status_code, 302)

    def test_user_news_list_view_authorized(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('news:my_news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/user_news_list.html')

    def test_create_newspaper_view(self):
        self.client.login(username='testuser', password='testpass123')
        image_path = os.path.join('media', 'news_images', 'culture.jpeg')
        with open(image_path, 'rb') as img:
            response = self.client.post(
                reverse('news:create'),
                {
                    'title': 'New Test News',
                    'description': 'New Description',
                    'content': 'New Content',
                    'topics': [self.topic.id],
                    'image': SimpleUploadedFile(
                        name='culture.jpeg',
                        content=img.read(),
                        content_type='image/jpeg'
                    )
                }
            )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Newspaper.objects.filter(title='New Test News').exists()
        )

    def test_search_news(self):
        response = self.client.get(
            reverse('news:index'),
            {'q': 'Test News'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test News')

class AccountsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_page_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_register_page_loads(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_login_with_valid_credentials(self):
        get_user_model().objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@test.com',
            years_of_experience=1
        )
        login_successful = self.client.login(
            username='testuser',
            password='testpass123'
        )
        self.assertTrue(login_successful)

    def test_register_with_valid_data(self):
        initial_user_count = get_user_model().objects.count()
        response = self.client.post(
            reverse('accounts:register'),
            {
                'username': 'newuser',
                'email': 'new@test.com',
                'password1': 'complex_password_123',
                'password2': 'complex_password_123',
                'years_of_experience': 1
            },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(get_user_model().objects.count(), initial_user_count + 1)

    def test_profile_edit_view(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@test.com',
            years_of_experience=1
        )
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(
            reverse('accounts:profile_edit'),
            {
                'first_name': 'Updated',
                'last_name': 'Name',
                'email': 'updated@test.com',
                'years_of_experience': 2
            }
        )
        self.assertEqual(response.status_code, 302)
        user.refresh_from_db()
        self.assertEqual(user.first_name, 'Updated') 