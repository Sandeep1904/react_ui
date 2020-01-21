from rest_framework import routers
from .api import LeadView

router = routers.DefaultRouter()
router.register('api/leads', LeadView, 'leads')

urlpatterns = router.urls
