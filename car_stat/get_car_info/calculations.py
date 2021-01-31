from django.db.models import Avg

import datetime
import calendar

from .models import *

def data_for_plot(brand, model, year_manufacture):
    plot_data={}
    price_list = []
    month_list = []
    quantity_list = []

    vehicles, gen = Vehicle.objects.filter_car_with_gen(brand=brand, model=model, year_manufacture=year_manufacture)
    whole_avg_price = format(round(vehicles.aggregate(Avg('price')).get('price__avg'), -2), '.2f')
    mindate = Vehicle.objects.get_earliest_date(brand, model)
    avg_mileage = format(round(vehicles.aggregate(Avg('mileage')).get('mileage__avg'), -2), '.2f')
    personal_seller = round(vehicles.filter(seller_type__name='Частное лицо').count()/vehicles.count(), 2) * 100

    now = datetime.datetime.now()
    start = 12 * int(mindate.year) + int(mindate.month) - 1
    finish = 12 * int(now.year) + int(now.month)

    for step in range(start, finish):
        year, month = divmod(step, 12)
        vv = vehicles.filter(date_create__year=year, date_create__month=month + 1)

        try:
            avg_price = format(round(vv.aggregate(Avg('price')).get('price__avg'), -2), '.2f')
        except:
            avg_price = whole_avg_price
        price_list.append(avg_price)

        total = vv.count()
        quantity_list.append(total)

        cur = str(calendar.month_name[month + 1]) + ', ' + str(year)
        month_list.append(cur)

        plot_data['quantity_list'] = quantity_list
        plot_data['price_list'] = price_list
        plot_data['month_list'] = month_list
        plot_data['whole_avg_price'] = whole_avg_price
        plot_data['generation'] = gen
        plot_data['avg_quantity'] = round(sum(quantity_list)/len(quantity_list))
        plot_data['avg_mileage'] = avg_mileage
        plot_data['personal_seller'] = personal_seller

    return plot_data