from django.db import models


class NewManager(models.Manager):
    def get_earliest_date(self, brand, model):
        return self.filter(brand=brand).filter(model=model).earliest('date_create').date_create


class VehicleBrand(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

class VehicleModel(models.Model):
    name = models.CharField(max_length=128, unique=True)
    brand = models.ForeignKey(VehicleBrand, on_delete=models.PROTECT, blank=True, null=True)

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


