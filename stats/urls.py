from rest_framework import routers

from stats.api import ClickViewSet

router = routers.DefaultRouter()
router.register('', ClickViewSet, 'clicks')

urlpatterns = router.urls
