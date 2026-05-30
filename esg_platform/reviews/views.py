from rest_framework import viewsets
from .models import DataIssue, RecordReview
from .serializers import (
    DataIssueSerializer,
    RecordReviewSerializer
)


class DataIssueViewSet(viewsets.ModelViewSet):
    queryset = DataIssue.objects.all()
    serializer_class = DataIssueSerializer


class RecordReviewViewSet(viewsets.ModelViewSet):
    queryset = RecordReview.objects.all()
    serializer_class = RecordReviewSerializer