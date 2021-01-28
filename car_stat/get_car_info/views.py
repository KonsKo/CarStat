from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404

import datetime

from .forms import StartForm
from .models import *



class StartView(FormView):
    form_class = StartForm
    template_name = 'get_car_info/start.html'
    success_url = reverse_lazy('start')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            brand = form.cleaned_data.get('brand')
            model = form.cleaned_data.get('model')
            return redirect(reverse_lazy('info', kwargs={'brand':brand, 'model':model}))
        return render(request, self.template_name, {'form': form})

class InfoView(ListView):
    template_name = 'carstat/brandmodel.html'

    def get_queryset(self):
        self.brand = get_object_or_404(VehicleBrand, name=self.kwargs['brand'])
        self.model = get_object_or_404(VehicleModel, name=self.kwargs['model'])
        return Vehicle.objects.filter(brand=self.brand).filter(model=self.model)

    def get_context_data(self, *args, **kwargs):
        context = super(InfoView, self).get_context_data(*args, **kwargs)
        self.brand = get_object_or_404(VehicleBrand, name=self.kwargs['brand'])
        self.model = get_object_or_404(VehicleModel, name=self.kwargs['model'])
        vehicles = Vehicle.objects.filter(brand=self.brand).filter(model=self.model)
        #mindate = vehicles.earliest('date_create').date_create
        mindate = Vehicle.objects.get_earliest_date(self.brand, self.model)
        print(mindate)
        now = datetime.datetime.now()
        start = 12 * int(mindate.year) + int(mindate.month)-1
        finish = 12 * int(now.year) + int(now.month)
        print(start, finish)
        price_list = []
        month_list = []
        for step in range(start, finish):
            year, month = divmod(step, 12)
            vv = vehicles.filter(date_create__year=year).filter(date_create__month=month+1)
            avg_price = vv.aggregate(Avg('price'))
            total = vv.count()
            price_list.append(avg_price.get('price__avg'))
            cur = str(month+1)+' month ' +str(year)
            month_list.append(cur)
            print(year, month+1, avg_price, total)
        print(month_list, price_list)
        context['test'] = mindate
        context['price_list'] = price_list
        context['month_list'] = month_list
        return context


def load_models(request):
    brand_id = request.GET.get('brand_id')
    models = VehicleModel.objects.filter(brand_id=brand_id).all()
    return render(request, 'carstat/model_dropdown_list_options.html', {'models': models})
