from .views import index, item_page
from django.urls import path

urlpatterns = [
    path('home/', view = index, name='index'),
    path('item/', view=item_page, name='item_page'),
]