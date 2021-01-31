from django.views.generic.edit import FormView
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404

import datetime

from .forms import StartForm
from .models import *
from .calculations import *


class StartView(FormView):
    form_class = StartForm
    template_name = 'get_car_info/start.html'
    success_url = reverse_lazy('start')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            brand = form.cleaned_data.get('brand')
            model = form.cleaned_data.get('model')
            year_manufacture = form.cleaned_data.get('year_manufacture')
            self.request.session['year'] = year_manufacture

            return redirect(reverse_lazy('info', kwargs={'brand':brand,'model':model,}))
        return render(request, self.template_name, {'form': form})

class InfoView(TemplateView):
    template_name = 'get_car_info/brandmodel.html'

    def get_context_data(self, *args, **kwargs):
        context = super(InfoView, self).get_context_data(*args, **kwargs)
        self.brand = get_object_or_404(VehicleBrand, name=self.kwargs['brand'])
        self.model = get_object_or_404(VehicleModel, name=self.kwargs['model'])
        year_manufacture = self.request.session['year']
        data = data_for_plot(brand=self.brand, model=self.model, year_manufacture=year_manufacture)
        context['quantity_list'] = data.get('quantity_list')
        context['price_list'] = data.get('price_list')
        context['month_list'] = data.get('month_list')
        context['avg_price'] = data.get('whole_avg_price')
        context['year_manufacture'] = year_manufacture
        context['generation'] = data.get('generation')
        context['avg_quantity'] = data.get('avg_quantity')
        context['avg_mileage'] = data.get('avg_mileage')
        context['personal_seller'] = data.get('personal_seller')
        return context

def load_models(request):
    brand_id = request.GET.get('brand_id')
    models = VehicleModel.objects.filter(brand_id=brand_id).all()
    return render(request, 'get_car_info/model_dropdown_list_options.html', {'models': models})
