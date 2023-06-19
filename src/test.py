from unittest import TestCase
from adapter.easybroker import apiConsult

class TestGetOrganization(TestCase):
   def test_get_organization_properties(self):
       responses = apiConsult.get_organization_properties()
       self.assertIsNotNone(responses)
       