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
            user=self.user
        )

        self.client.force_authenticate(user=self.user)

    def test_create_ad(self):
        """ Тест создания объявления """

        self.client.force_authenticate(user=self.user)
        user = User.objects.create(email='test1@test.com', role='User')
        user.set_password('08030803A')
        user.save()
        data = {
            "email": "test1@test.com",
            "password": "08030803A"
        }
        user_response = self.client.post(
            "/api/api/token/",
            data=data
        )

        token = user_response.data['access']
        data = {
            "title": "Test_ad",
            "price": 1500,
            "user": 1,
            "description": "test_ad",

        }
        response = self.client.post(
            "/api/api/ads/",
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Ad.objects.all().count() > 0)
        self.assertEqual(response.json()["description"], "test_ad")

    def test_list_ad(self):
        """ Тест вывода списка объявлений """

        user = User.objects.create(email='test2@test.com',
                                   password='08030803A', role='User')
        Ad.objects.create(title="Test list", price=1000,
                          description="test list", user=user)
        response = self.client.get(
            '/api/api/ads/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_ad(self):
        """ Тест обновления объявления """

        user = User.objects.create(email='test3@test.com')
        user.set_password('08030803A')
        user.save()
        data = {
            "email": "test3@test.com",
            "password": "08030803A"
        }
        user_response = self.client.post(
            "/api/api/token/",
            data=data
        )
        token = user_response.data['access']

        Ad.objects.create(title="Test update", price=1500,
                          description="test_update", user=user)

        data = {
            "title": "Test update update",
            "price": 15000,
        }

        response = self.client.patch(
            '/api/api/ads/5/',
            data=data,
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(
            '/api/api/ads/5/',
            headers={"Authorization": f"Bearer {token}"}
        )

        queryset = Ad.objects.all()
        self.assertTrue(len(queryset) == 1)

    def tearDown(self):
        User.objects.all().delete()
        Ad.objects.all().delete()
        return super().tearDown()


# class CommentTestCase(APITestCase):
#
#     def setUp(self) -> None:
#         pass
#
#     def test_create_comment(self):
#         """
#         тест создания комментария
#         """
#         user = User.objects.create(email='dada@test.com', role='User')
#         user.set_password('edcrfvtgb')
#         user.save()
#         data1 = {
#             "email": "dada@test.com",
#             "password": "edcrfvtgb"
#         }
#         user_response = self.client.post(
#             "/auth/jwt/create/",
#             data=data1
#         )
#         token = user_response.data['access']
#
#         Ad.objects.create(title="ASDASDASD", price=15, description="sadasdasd", author=user)
#         data = {
#             "text": "ASDASDASD",
#         }
#         response = self.client.post(
#             "/api/ads/4/comments/create/",
#             data=data,
#             headers={"Authorization": f"Bearer {token}"}
#         )
#
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#         self.assertTrue(Ad.objects.all().count() > 0)
#
#     def test_list_comment(self):
#         """
#         тест вывода списка комментариев
#         """
#         user = User.objects.create(email='sutulaya_sobaka@test.com', password='wdzxczxyty')
#         user.set_password('wdzxczxyty')
#         user.save()
#         data1 = {
#             "email": "sutulaya_sobaka@test.com",
#             "password": "wdzxczxyty"
#         }
#         user_response = self.client.post(
#             "/auth/jwt/create/",
#             data=data1
#         )
#         token = user_response.data['access']
#         ad = Ad.objects.create(title="ASDASDASD", price=15, description="sadasdasd", author=user)
#         Comment.objects.create(text="ASDASDASD", ad=ad, author=user)
#         response = self.client.get(
#             '/api/ads/5/comments/',
#             headers={"Authorization": f"Bearer {token}"}
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_update_comment(self):
#         """
#         тест обновления комментария
#         """
#         user = User.objects.create(email='dadada@test.com', password='edcrfvtgb', role='User')
#         user.set_password('edcrfvtgb')
#         user.save()
#         data1 = {
#             "email": "dadada@test.com",
#             "password": "edcrfvtgb"
#         }
#         user_response = self.client.post(
#             "/auth/jwt/create/",
#             data=data1
#         )
#         token = user_response.data['access']
#         ad = Ad.objects.create(title="ASDASDASD", price=15, description="sadasdasd", author=user)
#         Comment.objects.create(text="ASDASDASD", ad=ad, author=user)
#
#         data = {
#             "text": "TFEWFWF"
#         }
#
#         response = self.client.patch(
#             '/api/ads/6/comments/3/upd/',
#             data=data,
#             headers={"Authorization": f"Bearer {token}"}
#         )
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         self.client.delete(
#             '/api/ads/6/comments/3/delete/',
#             headers={"Authorization": f"Bearer {token}"}
#         )
#         queryset = Comment.objects.all()
#         self.assertTrue(len(queryset) == 0)
#
#     def tearDown(self):
#         User.objects.all().delete()
#         Ad.objects.all().delete()
#         return super().tearDown()
