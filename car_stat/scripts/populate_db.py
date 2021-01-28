from get_car_info.models import Vehicle

import pandas as pd


def run():
    file = '/home/cat/ProjectsGit/for_stat_project_for_create_new_one/vehicle.csv'
    df = pd.read_csv(file)
    for index, row in df.iterrows():
        Vehicle.objects.create(pk=int(row['id']),
                               link=str(row['link']),
                               date_create=row['date_create'],
                               # date_finished=row['date_finished'],
                               price=int(row['price']),
                               brand_id=int(row['brand_id']),
                               model_id=int(row['model_id']),
                               generation_id=int(row['generation_id']),
                               modification=(row['modification']),
                               year_manufacture=int(row['year_manufacture']),
                               mileage=int(row['mileage']),
                               condition_id=int(row['condition_id']),
                               quantity_owner=str(row['quantity_owner']),
                               body_type_id=int(row['body_type_id']),
                               quantity_doors=int(row['quantity_doors']),
                               engine_type_id=int(row['engine_type_id']),
                               transmission_id=int(row['transmission_id']),
                               drive_id=int(row['drive_id']),
                               wheel_id=int(row['wheel_id']),
                               color_id=int(row['color_id']),
                               equipment_id=int(row['equipment_id']),
                               address=str(row['address']),
                               region_id=int(row['region_id']),
                               city_id=int(row['city_id']),
                               seller_type_id=int(row['seller_type_id'])

                               )
