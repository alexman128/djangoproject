import json

from rest_framework.test import APITestCase
from django.urls import reverse

from notification.api.serializer import BackendUser
from notification.models import Category, Channel, BackendUser


class TestSetUp(APITestCase):
    def setUp(self):
        self.send_message_url = reverse('send_message')
        category1 = Category.objects.create(name="sports", description="Sports category")
        category2 = Category.objects.create(name="finance", description="Finance category")
        category3 = Category.objects.create(name="films", description="Films category")

        channel1 = Channel.objects.create(name="SMS", description="sends sms")
        channel2 = Channel.objects.create(name="email", description="sends email notification")
        channel3 = Channel.objects.create(name="push", description="sends push notification")

        user1 = BackendUser.objects.create(name="viviana", email="vivi123@gmail.com", phone="+523343777134")
        user2 = BackendUser.objects.create(name="rene martinez", email="remar123@gmail.com", phone="+523343667424")
        user3 = BackendUser.objects.create(name="victor cadena", email="vica123@gmail.com", phone="+523311474032")
        user4 = BackendUser.objects.create(name="david chong", email="david.chong@gmail.com", phone="+527223357495")
        user5 = BackendUser.objects.create(name="alex gonzalez", email="alex@gmail.com", phone="+527223357493")

        user1.subscribed_categories.set([category2])
        user1.channels.set([channel1])
        user2.subscribed_categories.set([category3])
        user2.channels.set([channel3])
        user3.subscribed_categories.set([category1])
        user3.channels.set([channel1])
        user4.subscribed_categories.set([category1, category2])
        user4.channels.set([channel1, channel2, channel3])
        user5.subscribed_categories.set([category3])
        user5.channels.set([channel2])

        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestViews(TestSetUp):
    def test_category_sent_does_not_exist(self):
        fixtures = ['/notification/fixtures/fixtures.json', ]
        message_content = "Hi, this is a sports message"
        message_category = "sports1"
        user_data = {
            "message_content": message_content,
            "message_category": message_category,
        }
        response_message = json.dumps({"User": "No subscribed users were found for that category."})
        res = self.client.post(self.send_message_url, user_data, format="json")
        self.assertEqual(res.status_code, 400)
        self.assertEqual(json.dumps(res.data), response_message)

    def test_category_sports_should_return_ok_status_and_response_data(self):
        fixtures = ['/notification/fixtures/fixtures.json', ]

        message_content = "Hi, this is a sports message"
        message_category = "sports"
        user_data = {
            "message_content": message_content,
            "message_category": message_category,
        }
        response_message = json.dumps({
            "Number of times each channel type was used to send the message to the users": [
                ["email", 1],
                ["push", 1],
                ["sms", 2]
            ]
        })

        res = self.client.post(self.send_message_url, user_data, format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), response_message)
