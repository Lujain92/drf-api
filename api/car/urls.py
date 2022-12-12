from django.urls import path
from .views import CarListView,CarDetailView
urlpatterns = [
   path('', CarListView.as_view(), name='Car_list'),
   path('<int:pk>', CarDetailView.as_view(),name='Car_detail')
]