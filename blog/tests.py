from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model(
                    ).objects.create_user(
                        username = "testuser",
                        email = "test@test.com",
                        password = "secret",
                    )
        self.post = Post.objects.create(
            title = "A title",
            body = "A body",
            author = self.user, 
        )

    def test_string_representation(self):
        post = Post(title="A sample title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A title")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.body}", "A body")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A body")
        self.assertTemplateUsed(response, "home.html")

    def test_post_detail_view(self):
        response = self.client.get("/posts/1/")
        no_response = self.client.get("/posts/1000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A title")
        self.assertTemplateUsed(response, "post_detail.html")    