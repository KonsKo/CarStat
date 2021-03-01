from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.ui import Select

from get_car_info.forms import StartForm
from get_car_info.models import *


class StartFormTest(TestCase):

    def setUp(self):
        self.brand1 = VehicleBrand.objects.create(name='brand1')
        self.brand2 = VehicleBrand.objects.create(name='brand2')
        self.model1 = VehicleModel.objects.create(name='model1', brand=self.brand1)
        self.model2 = VehicleModel.objects.create(name='model2', brand=self.brand1)
        self.model3 = VehicleModel.objects.create(name='model3', brand=self.brand2)
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
            year_manufacture = 2020,
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
            model=self.model2,
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
            brand=self.brand2,
            model=self.model3,
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


    # Test check logic only without dynamic content, it works if ignore form init.

    #def test_validation_logic_without_dynamic_content(self):
    #    form = StartForm(data={"brand": self.brand1, "model": self.model1, "year_manufacture": 2000})
    #    self.assertTrue(form.is_valid())
    #    form = StartForm(data={"brand": self.brand1, "model": self.model1, "year_manufacture": 3000})
    #    self.assertIn('Chosen year is too big, max year is 2021', form.errors.get('__all__'))
    #    form = StartForm(data={"brand": self.brand1, "model": self.model1, "year_manufacture": 10})
    #    self.assertIn('Chosen year is too low, min year is 2000', form.errors.get('__all__'))
    #    form = StartForm(data={"brand": self.brand1, "model": self.model1, "year_manufacture": 2005})
    #    self.assertIn('No cars for this filter', form.errors.get('__all__'))


class DynamicStartFormTest(StaticLiveServerTestCase):

    def setUp(self):
        self.brand1 = VehicleBrand.objects.create(name='brand1')
        self.brand2 = VehicleBrand.objects.create(name='brand2')
        self.model1 = VehicleModel.objects.create(name='model1', brand=self.brand1)
        self.model2 = VehicleModel.objects.create(name='model2', brand=self.brand1)
        self.model3 = VehicleModel.objects.create(name='model3', brand=self.brand2)
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
            year_manufacture = 2020,
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
            model=self.model2,
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
            brand=self.brand2,
            model=self.model3,
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

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_dynamic_logic(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/stat/start/'))

        # no brand chosen - zero models (value 1 is placeholder '---------')
        select_models = Select(self.selenium.find_element_by_name("model"))
        self.assertEqual(len(select_models.options), 1)
        self.assertEqual(select_models.options[0].text, '---------')

        # all brands (2) in options
        select_brands = Select(self.selenium.find_element_by_name("brand"))
        self.assertEqual(len(select_brands.options), 3)

        # choose 'brand1' - 2 models available 'model1' and 'model2'
        select_brands.select_by_visible_text('brand1')
        select_models = Select(self.selenium.find_element_by_name("model"))
        self.assertEqual(len(select_models.options), 3)
        self.assertIn('model1', [s.text for s in select_models.options])
        self.assertIn('model2', [s.text for s in select_models.options])

        # choose 'brand2' - 1 model available 'model3'
        select_brands.select_by_visible_text('brand2')
        select_models = Select(self.selenium.find_element_by_name("model"))
        self.assertEqual(len(select_models.options), 2)
        self.assertIn('model3', [s.text for s in select_models.options])

        select_models.select_by_visible_text('model3')

        #validation 'year_manufacture'
        year_manufacture = self.selenium.find_element_by_name('year_manufacture')
        year_manufacture.send_keys(1000)
        self.selenium.find_element_by_id('b_start').click()
        error = self.selenium.find_element_by_class_name('alert')
        self.assertIn('Chosen year is too low, min year is 2000', error.text)

        year_manufacture = self.selenium.find_element_by_name('year_manufacture')
        year_manufacture.clear()
        year_manufacture.send_keys(8000)
        self.selenium.find_element_by_id('b_start').click()
        error = self.selenium.find_element_by_class_name('alert')
        self.assertIn('Chosen year is too big, max year is 2021', error.text)

        year_manufacture = self.selenium.find_element_by_name('year_manufacture')
        year_manufacture.clear()
        year_manufacture.send_keys(2005)
        self.selenium.find_element_by_id('b_start').click()
        error = self.selenium.find_element_by_class_name('alert')
        self.assertIn('No cars for this filter', error.text)














