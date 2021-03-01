from django.test import TestCase

import datetime

from get_car_info.models import *

class ModelTest(TestCase):

    def setUp(self):
        self.brand1 = VehicleBrand.objects.create(name='brand1')
        self.model1 = VehicleModel.objects.create(name='model1', brand=self.brand1)
        self.generation1 = VehicleGeneration.objects.create(name='generation1')
        self.generation2 = VehicleGeneration.objects.create(name='generation2')
        self.condition1 = VehicleCondition.objects.create(name='condition1')
        self.body_type1 = VehicleBodyType.objects.create(name='bt1')
        self.engine_type1 = VehicleEngineType.objects.create(name='et1')
        self.transmission1 = VehicleTransmission.objects.create(name='transmission1')
        self.drive1 = VehicleDrive.objects.create(name='drive1')
        self.wheel1 = VehicleWheel.objects.create(name='wheel1')
        self.color1 = VehicleColor.objects.create(name='color1')
        self.equipment1 = VehicleEquipment.objects.create(name='equipment1')
        self.region1 = Region.objects.create(name='region1')
        self.city1 = City.objects.create(name='city1', region=self.region1)
        self.seller_type1 = VehicleSellerType.objects.create(name='st1')
        self.vehicle1 = Vehicle.objects.create(
            link='https://www.avito.ru/petrozavodsk/avtomobili/skoda_octavia_2015_2083975790_1',
            date_create = datetime.datetime(2020, 11, 14),
            price = 100000,
            brand = self.brand1,
            model = self.model1,
            generation = self.generation1,
            modification = 'modification1',
            year_manufacture = 2000,
            mileage = 100000,
            condition = self.condition1,
            quantity_owner = 1,
            body_type = self.body_type1,
            quantity_doors = 4,
            engine_type =  self.engine_type1,
            transmission = self.transmission1,
            drive = self.drive1,
            wheel = self.wheel1,
            color = self.color1,
            equipment = self.equipment1,
            address = 'address1',
            region = self.region1,
            city = self.city1,
            seller_type = self.seller_type1
        )
        self.vehicle2 = Vehicle.objects.create(
            link='https://www.avito.ru/petrozavodsk/avtomobili/skoda_octavia_2015_2083975790_2',
            date_create=datetime.datetime(2010, 11, 14),
            price=100000,
            brand=self.brand1,
            model=self.model1,
            generation=self.generation2,
            modification='modification1',
            year_manufacture=2000,
            mileage=100000,
            condition=self.condition1,
            quantity_owner=1,
            body_type=self.body_type1,
            quantity_doors=4,
            engine_type=self.engine_type1,
            transmission=self.transmission1,
            drive=self.drive1,
            wheel=self.wheel1,
            color=self.color1,
            equipment=self.equipment1,
            address='address1',
            region=self.region1,
            city=self.city1,
            seller_type=self.seller_type1
        )
        self.vehicle3 = Vehicle.objects.create(
            link='https://www.avito.ru/petrozavodsk/avtomobili/skoda_octavia_2015_2083975790_3',
            date_create=datetime.datetime(2010, 11, 13),
            price=100000,
            brand=self.brand1,
            model=self.model1,
            generation=self.generation1,
            modification='modification1',
            year_manufacture=2000,
            mileage=100000,
            condition=self.condition1,
            quantity_owner=1,
            body_type=self.body_type1,
            quantity_doors=4,
            engine_type=self.engine_type1,
            transmission=self.transmission1,
            drive=self.drive1,
            wheel=self.wheel1,
            color=self.color1,
            equipment=self.equipment1,
            address='address1',
            region=self.region1,
            city=self.city1,
            seller_type=self.seller_type1
        )

    def test_NewManager_get_earliest_date(self):
        earliest_date = Vehicle.objects.get_earliest_date(self.brand1, self.model1)
        self.assertEqual(earliest_date.date(), self.vehicle3.date_create.date())

    def test_NewManager_filter_car_with_gen(self):
        vehicles_with_gen, gen = Vehicle.objects.filter_car_with_gen(self.brand1, self.model1, 2000)
        self.assertEqual(len(vehicles_with_gen), 2)
        self.assertEqual(gen[0], self.generation1.name)
        self.assertEqual(gen[1], self.generation2.name)







