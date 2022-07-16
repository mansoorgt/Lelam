from django.urls import path
from .import views

urlpatterns = [
    path('Main_blank',views.RenderSide,name='Mainside'),
    path('',views.Events,name='events'),
    path('Trade',views.Tradepage,name='trade')
]
