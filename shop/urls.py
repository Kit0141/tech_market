from django.views.generic import TemplateView
from shop import views as v
from django.urls import path
urlpatterns = [
    # path('template_view/', TemplateView.as_view(template_name="template_view.html"), name='template_view'),
    path('about/', v.about, name='about'),
    path('contact/', v.contact, name='contact'),
    path('brand/', v.brand, name='brand'),
    path('special/', v.special, name='special'),
    # path('sum_view/', v.sum_view, name='contact'),
    # path('sum/', v.sum_two_nums, name='contact'),
    path('', v.index, name='index'),
]
