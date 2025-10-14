from django.test import TestCase, Client


class PollsSmokeTests(TestCase):
    def test_index_ok(self):
        c = Client()
        r = c.get("/polls/")
        self.assertIn(r.status_code, (200, 302))
