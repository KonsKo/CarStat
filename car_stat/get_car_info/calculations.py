from django.db.models import Avg

import datetime
import calendar

from .models import *

def data_for_plot(brand, model, year_manufacture):
    plot_data={}
    vehicles = Vehicle.objects.filter(brand=brand).filter(model=model).filter(year_manufacture=year_manufacture)
    mindate = Vehicle.objects.get_earliest_date(brand, model)
    now=datetime.datetime.now()
    start = 12 * int(mindate.year) + int(mindate.month) - 1
    finish = 12 * int(now.year) + int(now.month)
    price_list = []
    month_list = []
    quantity_list = []
    for step in range(start, finish):
        year, month = divmod(step, 12)
        vv = vehicles.filter(date_create__year=year).filter(date_create__month=month + 1)

        avg_price = vv.aggregate(Avg('price'))
        price_list.append(avg_price.get('price__avg'))

        total = vv.count()
        quantity_list.append(total)

        cur = str(calendar.month_name[month + 1]) + ', ' + str(year)
        month_list.append(cur)

        plot_data['quantity_list'] = quantity_list
        plot_data['price_list'] = price_list
        plot_data['month_list'] = month_list

    return plot_data