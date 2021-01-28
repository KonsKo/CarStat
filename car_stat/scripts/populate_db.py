from get_car_info.models import VehicleBodyType

import pandas as pd

def run():
    file = '/home/cat/ProjectsGit/for_stat_project_for_create_new_one/vehiclebodytype.csv'
    df = pd.read_csv(file)
    for index, row in df.iterrows():
        VehicleBodyType.objects.create(pk=int(row['id']), name=str(row['name']))


