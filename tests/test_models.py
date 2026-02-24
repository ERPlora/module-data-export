"""Tests for data_export models."""
import pytest
from django.utils import timezone

from data_export.models import DataJob


@pytest.mark.django_db
class TestDataJob:
    """DataJob model tests."""

    def test_create(self, data_job):
        """Test DataJob creation."""
        assert data_job.pk is not None
        assert data_job.is_deleted is False

    def test_str(self, data_job):
        """Test string representation."""
        assert str(data_job) is not None
        assert len(str(data_job)) > 0

    def test_soft_delete(self, data_job):
        """Test soft delete."""
        pk = data_job.pk
        data_job.is_deleted = True
        data_job.deleted_at = timezone.now()
        data_job.save()
        assert not DataJob.objects.filter(pk=pk).exists()
        assert DataJob.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, data_job):
        """Test default queryset excludes deleted."""
        data_job.is_deleted = True
        data_job.deleted_at = timezone.now()
        data_job.save()
        assert DataJob.objects.filter(hub_id=hub_id).count() == 0


