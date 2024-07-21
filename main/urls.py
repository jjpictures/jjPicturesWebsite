from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('gear/', views.gear, name='gear'),
    path('contact/', views.contact, name='contact'),
    path('project/<int:id>/', views.project_detail, name='project_detail'),
]
