from django.test import TestCase
from django.core.urlresolvers import resolve
from home.views import index
from home.apps import HomeConfig
from django.http import HttpRequest


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_root_url_returns_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))


class HomeAppTest(TestCase):
    def test_app_config_returns_home(self):
        self.assertEqual('home', HomeConfig.name)
