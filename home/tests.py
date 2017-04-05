from django.test import TestCase
from django.core.urlresolvers import resolve
from home.views import index
from home.apps import HomeConfig
from django.http import HttpRequest


class HomeAppTest(TestCase):
    def test_app_config_returns_home(self):
        self.assertEqual('home', HomeConfig.name)
