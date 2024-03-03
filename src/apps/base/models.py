import uuid

from django.db import models

from apps.base.managers import BaseManager


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, help_text="ID"
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Created At")
    updated_at = models.DateTimeField(auto_now=True, help_text="Updated At")
    deleted = models.BooleanField(default=False)

    objects = BaseManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        """
        We don't delete any record, we just mark it as deleted.
        """

        self.deleted = True
        self.save()
