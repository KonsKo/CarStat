from selenium import webdriver
from bs4 import BeautifulSoup
import re

from accounts.models import *

def run():
    element='https://www.avito.ru/petrozavodsk/avtomobili/lada_4x4_niva_2020_2058718250'

    if Vehicle.objects.filter(link=element).exists():
        print('exist')

    else:
        driver = webdriver.Chrome()
        driver.get(element)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        car_dic = {}

       # try:
        for ss in soup.find_all(class_='item-params-list-item'):
            s = str(ss.getText())
            s = s.replace(' ', '')
            x = re.split(':', s)
            car_dic[x[0]] = x[1]

        v_price = soup.find(class_='js-item-price').getText()
        v_price = v_price.replace(' ','')

        brand = car_dic.get('Марка')
        v_brand, created = VehicleBrand.objects.get_or_create(name=brand)

        model = car_dic.get('Модель')
        v_model, created = VehicleModel.objects.get_or_create(name=model)

        generation = car_dic.get('Поколение')
        v_generation, created = VehicleGeneration.objects.get_or_create(name=generation)

        v_modification = car_dic.get('Модификация')

        v_year_manufacture = car_dic.get('Годвыпуска')

        try:
            v_mileage = car_dic.get('Пробег')
            v_mileage = re.sub(r"\D", "", v_mileage)
        except:
            v_mileage = 0

        condition = car_dic.get('Состояние')
        v_condition, created = VehicleCondition.objects.get_or_create(name=condition)

        v_quantity_owner = car_dic.get('ВладельцевпоПТС')

        body_type = car_dic.get('Типкузова')
        v_body_type, created = VehicleBodyType.objects.get_or_create(name=body_type)

        v_quantity_doors = car_dic.get('Количестводверей')

        engine_type = car_dic.get('Типдвигателя')
        v_engine_type, created = VehicleEngineType.objects.get_or_create(name=engine_type)

        transmission = car_dic.get('Коробкапередач')
        v_transmission, created = VehicleTransmission.objects.get_or_create(name=transmission)

        drive = car_dic.get('Привод')
        v_drive, created = VehicleDrive.objects.get_or_create(name=drive)

        wheel = car_dic.get('Руль')
        v_wheel, created = VehicleWheel.objects.get_or_create(name=wheel)

        color = car_dic.get('Цвет')
        v_color, created = VehicleColor.objects.get_or_create(name=color)


        try:
            equipment = car_dic.get('Комплектация')
            v_equipment, created = VehicleEquipment.objects.get_or_create(name=equipment)
        except:
            equipment = 'Базовая'
            v_equipment, created = VehicleEquipment.objects.get_or_create(name=equipment)

        v_address = soup.find(class_='item-address__string').getText()

        #try:

        if 'Частное лицо' in soup.find(class_='item-view-content-right').getText():
            v_seller_type, created = VehicleSellerType.objects.get_or_create(name='Частное лицо')
        elif 'Автодилер' in soup.find(class_='item-view-content-right').getText():
            v_seller_type, created = VehicleSellerType.objects.get_or_create(name='Автодилер')
        elif 'Официальный дилер' in soup.find(class_='item-view-content-right').getText():
            v_seller_type, created = VehicleSellerType.objects.get_or_create(name='Официальный дилер')

        vehicle = Vehicle(link=element, price=int(v_price), brand=v_brand, model=v_model,
                                      generation=v_generation, modification=v_modification,
                                      year_manufacture=v_year_manufacture, mileage=v_mileage,
                                      condition=v_condition, quantity_owner=v_quantity_owner,
                                      body_type=v_body_type, quantity_doors=v_quantity_doors,
                                      engine_type=v_engine_type, transmission=v_transmission,
                                      drive=v_drive, wheel=v_wheel, color=v_color, equipment=v_equipment,
                                      address=v_address, seller_type=v_seller_type)

        vehicle.save()


        #except:
           # print('Not a car:')