
from django.urls import path, include
from . import views

urlpatterns = [
    path('muellmelden', views.muellmelden ),
    path('eintraege', views.show_entries),
    path('neuer_eintrag', views.add_entry),
    path('fetch', views.fetch),
]
