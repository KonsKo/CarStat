from django import forms
from .models import *


class StartForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['brand', 'model']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = VehicleModel.objects.none()

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = VehicleModel.objects.filter(brand_id=brand_id).order_by('name')
            except (ValueError, TypeError):
                pass