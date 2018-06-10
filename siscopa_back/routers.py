from rest_framework import routers
from api import views

router = routers.DefaultRouter() 

router.register(r'Jogadores', views.JogadoresViewSet)
router.register(r'Time', views.TimesViewSet)
router.register(r'Grupos', views.GruposViewSet)
router.register(r'Partidas', views.PartidasViewSet)