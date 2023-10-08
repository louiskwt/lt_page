from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.post = Post.objects.create(
            title="Foo title",
            body="Nice body content",
            author=cls.user,)
        
    def test_post_model(self):
        self.assertEqual(self.post.title, "Foo title") 
        self.assertEqual(self.post.body, "Nice body content") 
        self.assertEqual(self.post.author.username, "testuser") 
        self.assertEqual(str(self.post), "Foo title") 
        self.assertEqual(self.post.get_absolute_url(), "/post/1/")
    
    def test_url_exists_at_correct_location_listview(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
    
    def test_url_exists_at_correct_location_detailview(self):
        res = self.client.get("/blogs/1/")
        self.assertEqual(res.status_code, 200)
    
    def test_listview_template(self):
        res = self.client.get("/")
        self.assertTemplateUsed(res, "home.html")
    
    def test_detailview_template(self):
        res = self.client.get("/blogs/1/")
        self.assertTemplateUsed(res, "post_detail.html")