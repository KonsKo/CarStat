from django import forms
from django.db.models import Min

from .models import *

import datetime


class StartForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model', 'year_manufacture', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = VehicleModel.objects.none()

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = VehicleModel.objects.filter(brand=brand_id).order_by('name')
            except (ValueError, TypeError):
                pass

    def clean(self):
        super().clean()
        brand = self.cleaned_data["brand"]
        model = self.cleaned_data["model"]
        year = self.cleaned_data["year_manufacture"]
        vehicles = Vehicle.objects.filter(brand=brand).filter(model=model)

        min_year = vehicles.aggregate(Min('year_manufacture')).get('year_manufacture__min')

        max_year = int(datetime.datetime.now().year)
        if year < min_year:
            raise forms.ValidationError('Chosen year is too low, min year is {}'.format(min_year))
        if year > max_year:
            raise forms.ValidationError('Chosen year is too big, max year is {}'.format(max_year))

        if vehicles.filter(year_manufacture=year).count() == 0:
            raise forms.ValidationError('No cars for this filter')

