from rest_framework.routers import DefaultRouter

from about.views import (ClinicView,
                         DoctorView,
                         GalleryView,
                         )

router = DefaultRouter()
router.register('clinic', ClinicView)
router.register('doctor', DoctorView)
router.register('gallery', GalleryView)
urlpatterns = router.urls
