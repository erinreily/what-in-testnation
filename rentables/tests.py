from django.test import TestCase
from django.core.urlresolvers import resolve
from rentables.apps import RentablesConfig
from rentables.models import Rentable


# Create your tests here.

class RentablesAppTest(TestCase):
    def test_app_config_has_app_name(self):
        self.assertTrue('rentables', RentablesConfig.name)


class RentablesRentableModelTest(TestCase):
    def test_string_representation(self):
        rentable = Rentable(title="This is a rentable", type="Book")
        self.assertEqual(str(rentable), rentable.title)
