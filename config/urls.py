from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BackgroundView, LicenseFieldView

router = DefaultRouter()
router.register('background', BackgroundView)
router.register('license', LicenseFieldView)

urlpatterns = router.urls
