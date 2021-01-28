from get_car_info.models import VehicleGeneration, Vehicle


def run():
    generations = VehicleGeneration.objects.all()
    vehicles = Vehicle.objects.all()

    for g in generations:
        try:
            brand = Vehicle.objects.filter(generation=g.id).first().brand
            g.brand = brand
            g.save()
            print(brand)
        except:
            g.delete()
