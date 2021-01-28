from get_car_info.models import City, Region

import pandas as pd

def run():
    file = '/home/cat/ProjectsGit/for_stat_project_for_create_new_one/vehiclecity.csv'
    df = pd.read_csv(file)
    for index, row in df.iterrows():
        #region = Region.objects.get(pk=row['region_id'])
        City.objects.create(pk=int(row['id']),
                              name=str(row['name']),
                              region_id=int(row['region_id']),
                            )


