from rest_framework.routers import DefaultRouter
from services.views import (
    ServicesView,
    ServicesItemsView,
)

router = DefaultRouter()

router.register('services', ServicesView)
router.register('serviceitems', ServicesItemsView)

urlpatterns = router.urls
