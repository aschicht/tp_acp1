"""tp_acp1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tp_acp1 import api, settings

router = routers.DefaultRouter()
router.register(r'medio-de-pago', api.MedioDePagoViewSet)
router.register(r'plato', api.PlatoViewSet)
router.register(r'filtro', api.FiltroViewSet)
router.register(r'promocion', api.PromocionViewSet)
router.register(r'menu-del-dia', api.MenuDelDiaViewSet)
router.register(r'sugerencia', api.SugerenciaViewSet)
router.register(r'categoria', api.CategoriaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('carta/', api.carta, name='carta'),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

admin.site.site_header = "Administracion de menu"
admin.site.site_title = "Menu web"
admin.site.index_title = "Bienvenido a la web de mi menu"
