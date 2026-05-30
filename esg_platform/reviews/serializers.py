from rest_framework import serializers
from .models import DataIssue, RecordReview


class DataIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataIssue
        fields = '__all__'


class RecordReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordReview
        fields = '__all__'