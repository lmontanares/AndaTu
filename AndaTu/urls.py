from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from delivery import views as delivery_view

from package import views as package_view
from auth_app import views as user_view
from delivery import views as delivery_view



router = DefaultRouter()
router.register(r'delivery',delivery_view.DeliveryViewSet)
router.register(r'delivery_detail',delivery_view.DeliveryDetailViewSet)
router.register(r'package', package_view.PackageViewSet)


urlpatterns = (
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    re_path(r"^auth/", include("djoser.urls.base")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
)
