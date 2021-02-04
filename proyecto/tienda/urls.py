from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.tienda, name="tienda"),
    path('carrito/', views.carrito, name="carrito"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)