from django.urls import path
from . import views 


app_name = 'labs'
urlpatterns = [
    # lab views    
    path('', views.LabListView.as_view(), name='lab_list'),
    path('<skill>/<slug:lab>/',
         views.lab_detail,
         name='lab_detail'),
] 