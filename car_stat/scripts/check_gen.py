from get_car_info.models import *

def run():
    vehicles = Vehicle.objects.all()
    brands = VehicleBrand.objects.all()
    models = VehicleModel.objects.all()

    for brand in brands:
        for model in models.filter(brand__name=brand):
            vehicles_b_m = vehicles.filter(brand=brand, model=model)
            years = vehicles_b_m.values_list('year_manufacture').distinct()
            # print(brand, model, years)

            for year in years:
                vehicles_b_m_y = vehicles_b_m.filter(year_manufacture=year[0])
                gen_list = vehicles_b_m_y.values_list('generation').distinct()
                if len(gen_list) > 1:
                    print(len(gen_list), brand, model, year)


