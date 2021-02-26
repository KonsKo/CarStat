from django.views.generic.edit import FormView
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404


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

        vehicles, gen = Vehicle.objects.filter_car_with_gen(brand=self.brand,
                                                            model=self.model,
                                                            year_manufacture=year_manufacture)
        if len(gen) > 1:
            context['gen_list'] = gen
        average_data = vehicles.aggregate(Avg('price'), Avg('mileage'))
        mindate = Vehicle.objects.get_earliest_date(self.brand, self.model)
        context['personal_seller'] = round(
            vehicles.filter(seller_type__name='Частное лицо').count() / vehicles.count(), 2
        ) * 100

        context['price_list'], context['month_list'], context['quantity_list'] = \
            create_month_statistics_list(vehicles, mindate, average_data.get('price__avg'))
        context['avg_price'] = format(round(average_data.get('price__avg'), -2), '.2f')
        context['year_manufacture'] = year_manufacture
        context['generation'] = gen.first()
        context['avg_quantity'] = round(
            sum(context['quantity_list']) / len(context['quantity_list'])
        )
        context['avg_mileage'] = format(round(average_data.get('mileage__avg'), -2), '.2f')

        return context

def load_models(request):
    brand_id = request.GET.get('brand_id')
    models = VehicleModel.objects.filter(brand_id=brand_id).all()
    return render(request, 'get_car_info/model_dropdown_list_options.html', {'models': models})
