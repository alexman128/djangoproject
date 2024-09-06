import json

from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self):
        self.send_message_url = reverse('send_message')
        load_data('fixture.json')

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
            "Number of times each channel type was used to send the message to the users": {
                "SMS": 2,
                "push": 1,
                "email": 1
            }
        })
        res = self.client.post(self.send_message_url, user_data, format="json")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.dumps(res.data), response_message)
