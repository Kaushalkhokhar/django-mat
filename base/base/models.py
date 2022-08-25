import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomBaseModelManager(models.Manager):
    def soft_delete(self, id, *args, **kwargs):
        return super().get_queryset().filter(pk=id).update(is_deleted=True)

    def soft_deletes(self, ids, *args, **kwargs):
        return super().get_queryset().filter(pk__in=ids).update(is_deleted=True)

class BaseModel(mdoels.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_deleted = models.BooleanField(default=False)
    ceated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    objects = CustomBaseModelManager()

    def save(self, *args, **kwargs):
        if not self.updated_at:
            self.updated_at = datetime.datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
