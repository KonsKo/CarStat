from django.db import models
from django.db.models import Avg

import datetime
import calendar


def create_month_statistics_list(vehicles, mindate, whole_avg_price):
    price_list = []
    month_list = []
    quantity_list = []
    now = datetime.datetime.now()
    start = 12 * int(mindate.year) + int(mindate.month) - 1
    finish = 12 * int(now.year) + int(now.month)
    for step in range(start, finish):
        year, month = divmod(step, 12)
        vv = vehicles.filter(date_create__year=year, date_create__month=month + 1)
        try:
            avg_price = format(round(vv.aggregate(Avg('price')).get('price__avg'), -2), '.2f')
        except:
            avg_price = format(round(whole_avg_price, -2), '.2f')
        price_list.append(avg_price)
        total = vv.count()
        quantity_list.append(total)
        cur = str(calendar.month_name[month + 1]) + ', ' + str(year)
        month_list.append(cur)

    return price_list, month_list, quantity_list


class NewManager(models.Manager):
    def get_earliest_date(self, brand, model):
        return self.filter(brand=brand).filter(model=model).earliest('date_create').date_create

    def filter_car_with_gen(self, brand, model, year_manufacture):
        vehicles_no_gen = Vehicle.objects.filter(brand__name=brand, model__name=model,
                                                 year_manufacture=year_manufacture)
        gen = vehicles_no_gen.values_list('generation__name', flat=True).distinct()
        vehicles_with_gen = Vehicle.objects.filter(brand=brand, model=model, generation__name=gen.first())
        #vehicles_with_gen = Vehicle.objects.filter(brand=brand, model=model, generation__name__in=gen)   # all generations
        return vehicles_with_gen, gen


class VehicleBrand(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]

class VehicleModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    brand = models.ForeignKey(VehicleBrand, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name

class VehicleGeneration(models.Model):
    name = models.CharField(max_length=128, unique=True)
    brand = models.ForeignKey(VehicleBrand, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name

class VehicleCondition(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class VehicleBodyType(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class VehicleEngineType(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class VehicleTransmission(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class VehicleDrive(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class VehicleWheel(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class VehicleColor(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class VehicleEquipment(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class VehicleSellerType(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=128, unique=True)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    link = models.CharField(max_length=256, unique=True, blank=False, null=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_finished = models.DateTimeField(blank=True, null=True)
    price = models.IntegerField(blank=False)
    brand = models.ForeignKey(VehicleBrand, on_delete=models.PROTECT)
    model = models.ForeignKey(VehicleModel, on_delete=models.PROTECT)
    generation = models.ForeignKey(VehicleGeneration, on_delete=models.PROTECT)
    modification = models.CharField(max_length=128, blank=True)
    year_manufacture = models.IntegerField(blank=False)
    mileage = models.IntegerField(blank=False)
    condition = models.ForeignKey(VehicleCondition, on_delete=models.PROTECT)
    quantity_owner = models.CharField(max_length=2, blank=False)
    body_type = models.ForeignKey(VehicleBodyType, on_delete=models.PROTECT)
    quantity_doors = models.IntegerField()
    engine_type = models.ForeignKey(VehicleEngineType, on_delete=models.PROTECT)
    transmission = models.ForeignKey(VehicleTransmission, on_delete=models.PROTECT)
    drive = models.ForeignKey(VehicleDrive, on_delete=models.PROTECT)
    wheel = models.ForeignKey(VehicleWheel, on_delete=models.PROTECT)
    color = models.ForeignKey(VehicleColor, on_delete=models.PROTECT)
    equipment = models.ForeignKey(VehicleEquipment, on_delete=models.PROTECT, blank=True, null=True)
    address = models.CharField(max_length=128)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True)
    seller_type = models.ForeignKey(VehicleSellerType, on_delete=models.PROTECT)

    objects = NewManager()

    def __str__(self):
        return self.link


