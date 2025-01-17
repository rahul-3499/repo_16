from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Employee
from django.urls import reverse_lazy

#views

class EmployeeListView(ListView):
    model = Employee


class EmployeeCreateView(CreateView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy('show_url')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy('show_url')

class EmployeeDeleteView(DeleteView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy('show_url')

