from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cuidadores import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.cadastro, name='cadastro'),
    path('painel/', views.dashboard, name='dashboard'),
    path('lista/', views.lista_cuidadores, name='lista'),
    path('exportar/', views.exportar_excel, name='exportar_excel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)