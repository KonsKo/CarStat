from django.test import TestCase

from get_car_info.models import *

class ModelTest(TestCase):

    def test_check_empty_fields_generation(self):
        vehicles = Vehicle.objects.all()
        empty_field_gen = 0
        for v in vehicles:
            if v.generation == None:
                empty_field_gen += 1
        self.assertIs(empty_field_gen, 0)





