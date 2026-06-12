from django.test import SimpleTestCase

class HomepageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutpageTest(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)