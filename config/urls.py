from rest_framework.routers import DefaultRouter

from config.views import (
    BackgroundView,
    LicenseFieldView,
)

router = DefaultRouter()
router.register('background', BackgroundView)
router.register('license', LicenseFieldView)

urlpatterns = router.urls
