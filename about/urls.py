from .views import ClinicView, DoctorView, GalleryView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('clinic', ClinicView)
router.register('doctor', DoctorView)
router.register('gallery', GalleryView)
urlpatterns = router.urls
