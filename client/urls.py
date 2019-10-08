from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('',views.get_clients,name='get_clients'), 
    path('client',views.client,name='client'), 
    path('base',views.base,name='base'),  
    path('get_client_profile/<int:id>',views.get_client_profile,name='get_client_profile'),  
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('update_client/<int:id>',views.update_client,name='update_client'),  

]
