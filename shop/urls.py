from shop import views as v
from django.urls import path
urlpatterns = [
    path('about/', v.about, name='about'),
    path('contact/', v.contact, name='contact'),
    path('sum/', v.sum_two_nums, name='contact'),
    path('', v.index, name='index'),
]
