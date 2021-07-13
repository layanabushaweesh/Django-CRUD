from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView ,  CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView


from django.urls import reverse_lazy
from .models import Snack

# Create your views here.
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ['title', 'purchaser', "description"]

   
class SnackUpdateView(UpdateView):
    template_name = "update.html"
    model = Snack
    fields = ['title', 'purchaser', "description"]

class SnackDeleteView(DeleteView):
    template_name = "delete.html"
    model = Snack
    success_url = reverse_lazy("snack_list")


