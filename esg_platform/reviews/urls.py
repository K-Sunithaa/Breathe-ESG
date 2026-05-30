from rest_framework.routers import DefaultRouter
from .views import DataIssueViewSet, RecordReviewViewSet

router = DefaultRouter()
router.register("issues", DataIssueViewSet)
router.register("reviews", RecordReviewViewSet)

urlpatterns = router.urls