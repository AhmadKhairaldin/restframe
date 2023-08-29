from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('match',views,basename="match")
