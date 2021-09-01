from django.test import TestCase
from django.test import RequestFactory
from .views import HomeView
# Create your tests here.
class HomepageTest(TestCase):
    def test_environment_set_in_context(self):
        request = RequestFactory().get('/')
        view = HomeView
        view.setup(request)
        context = view.get_context_data()
        self.assertIn('environment', context)
