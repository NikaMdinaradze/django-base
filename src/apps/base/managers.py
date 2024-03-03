from django.db import models


class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(deleted=True)

    def get_queryset_with_deleted_instances(self):
        return super().get_queryset()
