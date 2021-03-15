from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.
from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title='A good title',
            body="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Odit soluta, laudantium cum unde nesciunt reprehenderit incidunt delectus quisquam sit, inventore eius voluptatum distinctio mollitia laboriosam. Velit totam architecto error odio!",
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A good post!')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        # print(self.post)
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'test')
        self.assertEqual(f'{self.post.body}', "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Odit soluta, laudantium cum unde nesciunt reprehenderit incidunt delectus quisquam sit, inventore eius voluptatum distinctio mollitia laboriosam. Velit totam architecto error odio!")

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, 'Lorem ipsum dolor sit amet consectetur')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_view(self):
        response = self.client.get('/blog/post/1/')
        no_response = self.client.get('/blog/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

        #
        #
        #
        #
