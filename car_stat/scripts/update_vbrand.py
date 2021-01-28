from accounts.models import *

def run():
    models = VehicleModel.objects.all()

    for m in models:
        vehicle = Vehicle.objects.filter(model=m.id).first()
        try:
            m.brand = vehicle.brand
            m.save()

        except:

            print(vehicle, m)





