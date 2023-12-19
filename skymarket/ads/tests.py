from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from ads.models import Ad, Comment
from users.models import User


class AdTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
            is_active=True,
        )
        self.user.set_password('12345')
        self.user.save()
        self.client = APIClient()

        self.ad = Ad.objects.create(
            title='test',
            description='test',
            price=1000,
            author=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_create_ad(self):
        """ Тест создания объявления """

        data = {
            "email": "test@test.com",
            "password": "12345"
        }
        user_response = self.client.post(
            "/api/token/",
            data=data
        )

        token = user_response.data['access']
        data = {
            "title": "Test_ad",
            "price": 1500,
            "author": 1,
            "description": "test_ad",

        }
        response = self.client.post(
            "/api/ads/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Ad.objects.all().count() > 0)
        self.assertEqual(response.json()["description"], "test_ad")
        self.assertEqual(str(Ad.objects.get(pk=2)), "Test_ad")
        self.assertEqual(str(Ad.objects.get(pk=2).author), "test@test.com")

    def test_list_ad(self):
        """ Тест вывода списка объявлений """

        Ad.objects.create(title="Test list", price=1000,
                          description="test list", author=self.user)
        response = self.client.get(
            '/api/ads/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_ad(self):
        """ Тест обновления объявления """

        data = {
            "email": "test@test.com",
            "password": "12345"
        }
        user_response = self.client.post(
            "/api/token/",
            data=data
        )
        token = user_response.data['access']

        Ad.objects.create(title="Test update", price=1500,
                          description="test_update", author=self.user)

        data = {
            "title": "Test update update",
            "price": 15000,
        }

        response = self.client.patch(
            '/api/ads/5/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(
            '/api/ads/5/',
            headers={"Authorization": f"Bearer {token}"}
        )

        queryset = Ad.objects.all()
        self.assertTrue(len(queryset) == 1)

    def tearDown(self):
        User.objects.all().delete()
        Ad.objects.all().delete()
        return super().tearDown()


class CommentTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.com',
            is_active=True,
        )
        self.user.set_password('12345')
        self.user.save()
        self.client = APIClient()

        self.ad = Ad.objects.create(
            title='test',
            description='test',
            price=1000,
            author=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_create_comment(self):
        """ Тест создания комментария """

        data = {
            "email": "test@test.com",
            "password": "12345"
        }
        user_response = self.client.post(
            "/api/token/",
            data=data
        )

        token = user_response.data['access']

        Ad.objects.create(title="test_ad", price=1500, description="test_ad",
                          author=self.user)
        data = {
            "text": "comment",
        }
        response = self.client.post(
            "/api/ads/7/comments/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Ad.objects.all().count() > 0)
        self.assertEqual(str(Comment.objects.get(ad=7)), "comment")

    def test_list_comment(self):
        """ Тест вывода списка комментариев """

        data = {
            "email": "test@test.com",
            "password": "12345"
        }
        user_response = self.client.post(
            "/api/token/",
            data=data
        )

        token = user_response.data['access']

        ad = Ad.objects.create(title="test_ad", price=1500,
                               description="test_ad",
                               author=self.user)
        Comment.objects.create(text="comment_list", ad=ad, author=self.user)

        response = self.client.get(
            '/api/ads/8/comments/',
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        """ Тест обновления комментария """

        data = {
            "email": "test@test.com",
            "password": "12345"
        }

        user_response = self.client.post(
            "/api/token/",
            data=data
        )

        token = user_response.data['access']

        ad = Ad.objects.create(title="test_ad", price=1500,
                               description="test_ad",
                               author=self.user)
        Comment.objects.create(text="comment", ad=ad, author=self.user)

        data = {
            "text": "comment_update"
        }

        response = self.client.patch(
            '/api/ads/12/comments/3/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["text"], "comment_update")

        self.client.delete(
            '/api/ads/12/comments/3/',
            headers={"Authorization": f"Bearer {token}"}
        )
        queryset = Comment.objects.all()
        self.assertTrue(len(queryset) == 0)

    def tearDown(self):
        User.objects.all().delete()
        Ad.objects.all().delete()
        return super().tearDown()

