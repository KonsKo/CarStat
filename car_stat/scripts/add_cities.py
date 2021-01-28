from accounts.models import *

import re

def run():
    all_v = Vehicle.objects.all()
    bunch = []
    for v in all_v:
        link = v.link
        address = v.address
        pattern = r"www\.avito\.ru\/\w+\/"
        try:
            x = re.search(pattern, link)
            city = x.group().replace('www.avito.ru/', '').replace('/', '')
            if city not in bunch and 'Республика Карелия' in address:
                bunch.append(city)
        except:
            print(v)
    print(bunch)

    region=Region.objects.filter(name='karelia').first()
    for b in bunch:
        new_city = City(name=b)
        new_city.region = region
        new_city.save()