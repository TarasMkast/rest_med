from rest_framework.routers import DefaultRouter
from news.views import NewsView


router = DefaultRouter()
router.register('news', NewsView)
urlpatterns = router.urls
