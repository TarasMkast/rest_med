from django.urls import path
from .views import ServicesView, ServicesItemsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('services', ServicesView)
router.register('serviceitems', ServicesItemsView)

urlpatterns = router.urls
