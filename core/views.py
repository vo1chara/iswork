from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView
from .models import Domen
from .forms import DomenForm
from .utils import Domen_Create_Delete
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy



# Create your views here.

class  MainPageView(CreateView):
    model = Domen
    template_name="index.html"
    form_class = DomenForm
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        kwargs['list_domens'] = Domen.objects.all().order_by('-id')
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        domen_name = self.object.name
        web_server = self.object.webserver
        if web_server == 1:
            result = Domen_Create_Delete().create_domen_apache2(domen_name)
        elif web_server == 2:
            result = Domen_Create_Delete().create_domen_nginx(domen_name)
        if result:
            self.object.save()
        return super().form_valid(form)
    

class DomenDeleteView(DeleteView):
    model = Domen
    success_url = reverse_lazy('home')
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        domen_name = self.object.name
        web_server = self.object.webserver
        if web_server == 1:
            result = Domen_Create_Delete().delete_domen_apache2(domen_name)
        elif web_server == 2:
            result = Domen_Create_Delete().delete_domen_nginx(domen_name)
        if result:
            self.object.delete()
        return HttpResponseRedirect(self.success_url)
