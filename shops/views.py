from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from shops.models import Shop
from shops.forms import ShopForm
from django.views.generic import ListView, DetailView, TemplateView, CreateView


class ShopList(ListView):
    model = Shop
    context_object_name = 'shops'
    template_name = 'shops/all_shops.html'


class ShopDetail(DetailView):
    model = Shop
    context_object_name = 'shop'
    template_name = 'shops/shop_detail.html'


class ShopCreate(CreateView):
    model = Shop
    fields = '__all__'
    template_name = 'shops/shop_form.html'


class ShopEdit(TemplateView):
    template_name = 'shops/shop_form.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            context["form"].save()
            messages.success(request, 'success')
            return redirect('shop_edit', pk=self.kwargs['pk'])
        return super(TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(ShopEdit, self).get_context_data(**kwargs)
        form = ShopForm(self.request.POST or None, instance=get_object_or_404(Shop, pk=self.kwargs['pk']))
        context["form"] = form
        return context
