from django.urls import path
from .views import EmployeeListView, EmployeeCreateView,EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('add/', EmployeeCreateView.as_view(), name = 'add_url'),
    path('show/', EmployeeListView.as_view(), name = 'show_url'),
    path('update/<pk>/', EmployeeUpdateView.as_view(), name = 'update_url'),
    path('delete/<pk>/', EmployeeDeleteView.as_view(), name = 'delete_url')
]