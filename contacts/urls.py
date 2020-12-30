from rest_framework.routers import DefaultRouter
from contacts.views import (
    SocialView,
    MapMarkerView,
    ContactsView,
)

router = DefaultRouter()

#router.register('appointment/', AppointmentView)
router.register('social', SocialView)
router.register('mapmarker', MapMarkerView)
router.register('contacts', ContactsView)

urlpatterns = router.urls
