import unittest

from pyramid import testing


class TutorialFunctionalTests(unittest.TestCase):
    def setUp(self):
        from backend import main
        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_home(self):
        res = self.testapp.get('/', status=200)
        self.assertIn(b'<app-root>', res.body)
