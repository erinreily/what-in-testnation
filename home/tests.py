from django.test import TestCase
from django.core.urlresolvers import resolve
from home.views import index
from home.apps import HomeConfig
from django.http import HttpRequest


class HomeAppTest(TestCase):
    def test_app_config_returns_home(self):
        self.assertEqual('home', HomeConfig.name)
<<<<<<< HEAD


class HomeViewsTest(TestCase):

    def test_root_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)
=======
>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b
