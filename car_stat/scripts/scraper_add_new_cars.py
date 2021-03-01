from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
import random

from get_car_info.models import *


def run():

    counter = 0
    link_start = 'https://www.avito.ru/kareliya/avtomobili?s=104&p='

    driver = webdriver.Chrome()
    elements = []

    for page in range(1, 11):
        link = link_start + str(page)
        driver.get(link)
        search = driver.find_elements_by_class_name('link-link-39EVK')
        for s in search:
            pattern = 'https\:\/\/www\.avito\.ru\/(\w+)\/avtomobili\/(\w+)'
            element_link = str(s.get_attribute('href'))
            if not re.search(pattern, element_link):
                continue
            elif not City.objects.filter(name=re.search(pattern, element_link).group(1)).exists():
                #print('Skip, not RK', re.search(pattern, element_link).group(1))
                continue
            if not Vehicle.objects.filter(link=element_link).exists():
                elements.append(element_link)

    for element in elements:
        if element == None:
            continue
        if 'avito.ru' not in element:
            continue
        if Vehicle.objects.filter(link=element).exists():
            continue
        else:
            driver.get(element)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            car_dic = {}
            try:
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
                if VehicleModel.objects.filter(name=model).exists():
                    v_model = VehicleModel.objects.get(name=model)
                else:
                    new_model = VehicleModel.objects.create(name=model, brand=v_brand)
                    v_model = new_model

                generation = car_dic.get('Поколение')
                if VehicleGeneration.objects.filter(name=generation).exists():
                    v_generation = VehicleGeneration.objects.get(name=generation)
                else:
                    new_generation = VehicleGeneration.objects.create(name=generation, brand=v_brand)
                    v_generation = new_generation

                v_modification = car_dic.get('Модификация')

                v_year_manufacture = car_dic.get('Годвыпуска')

                try:
                    v_mileage = car_dic.get('Пробег')
                    v_mileage = re.sub(r"\D", "", v_mileage)
                except:
                    v_mileage = 0

                if car_dic.get('Состояние'):
                    condition = car_dic.get('Состояние')
                    v_condition, created = VehicleCondition.objects.get_or_create(name=condition)
                else:
                    v_condition = VehicleCondition.objects.get(name='небитый')

                if car_dic.get('ВладельцевпоПТС'):
                    v_quantity_owner = car_dic.get('ВладельцевпоПТС')
                else:
                    v_quantity_owner = str(0)

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
                if 'Республика Карелия' not in v_address:
                    #print('***** Not RK', element)
                    continue

                v_region = Region.objects.get(name='karelia')

                pattern = 'https\:\/\/www\.avito\.ru\/([a-z\_]+)\/avtomobili\/'
                city = re.search(pattern, element).group(1)
                if City.objects.filter(name=city).exists():
                    v_city = City.objects.get(name=city)
                else:
                    new_city = City.objects.create(name=city, region=v_region)
                    v_city = new_city


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
                                  address=v_address, seller_type=v_seller_type,
                                  region=v_region, city=v_city)

                vehicle.save()
                counter +=1
                time.sleep(random.randint(2, 6))
                
            except:
                pass
                #print('Not a car:', element)

    print('Were added {} cars'.format(counter))