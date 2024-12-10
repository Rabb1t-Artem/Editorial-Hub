from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from news.forms import NewspaperForm, NewsSearchForm
from accounts.forms import UserRegistrationForm, UserProfileEditForm
from news.models import Topic
import os


class NewspaperFormTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Test Topic")

    def test_newspaper_form_valid_data(self):
        image_path = os.path.join("media", "news_images", "culture.jpeg")
        with open(image_path, "rb") as img:
            form_data = {
                "title": "Test Title",
                "description": "Test Description",
                "content": "Test Content",
                "topics": [self.topic.id],
            }
            file_data = {
                "image": SimpleUploadedFile(
                    name="culture.jpeg", content=img.read(), content_type="image/jpeg"
                )
            }
            form = NewspaperForm(data=form_data, files=file_data)
            if not form.is_valid():
                print(form.errors)
            self.assertTrue(form.is_valid())

    def test_newspaper_form_no_data(self):
        form = NewspaperForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            len(form.errors), 5
        )  # title, description, content, image, topics


class NewsSearchFormTest(TestCase):
    def setUp(self):
        self.topic = Topic.objects.create(name="Test Topic")

    def test_search_form_empty(self):
        form = NewsSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_search_form_with_query(self):
        form = NewsSearchForm(data={"q": "test search"})
        self.assertTrue(form.is_valid())

    def test_search_form_with_topics(self):
        form = NewsSearchForm(data={"topics": [self.topic.id]})
        self.assertTrue(form.is_valid())

    def test_search_form_with_all_params(self):
        form = NewsSearchForm(data={
            "q": "test search",
            "topics": [self.topic.id]
        })
        self.assertTrue(form.is_valid())


class UserFormsTest(TestCase):
    def test_registration_form_valid_data(self):
        form = UserRegistrationForm(
            data={
                "username": "testuser",
                "email": "test@test.com",
                "password1": "complex_password_123",
                "password2": "complex_password_123",
                "years_of_experience": 1,
            }
        )
        self.assertTrue(form.is_valid())

    def test_registration_form_passwords_dont_match(self):
        form = UserRegistrationForm(
            data={
                "username": "testuser",
                "email": "test@test.com",
                "password1": "complex_password_123",
                "password2": "different_password_123",
                "years_of_experience": 1,
            }
        )
        self.assertFalse(form.is_valid())

    def test_profile_edit_form_valid_data(self):
        form = UserProfileEditForm(
            data={
                "first_name": "Test",
                "last_name": "User",
                "email": "test@test.com",
                "years_of_experience": 2,
            }
        )
        self.assertTrue(form.is_valid())

    def test_profile_edit_form_invalid_email(self):
        form = UserProfileEditForm(
            data={
                "first_name": "Test",
                "last_name": "User",
                "email": "invalid-email",
                "years_of_experience": 2,
            }
        )
        self.assertFalse(form.is_valid())
