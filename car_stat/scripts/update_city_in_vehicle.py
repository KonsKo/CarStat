from accounts.models import *

def run():
    vehicles = Vehicle.objects.exclude(region=1)
    cities = City.objects.all()
    region = Region.objects.get(name='karelia')
    for v in vehicles:
        link = v.link
        for c in cities:
            city = c.name
            if city in link:
                v.city = c
                v.region = region
                v.save()
                continue
