
from rest_framework.routers import SimpleRouter
from ecom.views import ProductOperations

router = SimpleRouter()
router.register('apis',ProductOperations)

urlpatterns =router.urls