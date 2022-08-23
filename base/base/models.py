import datetime
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BaseModel(mdoels.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_deleted = models.BooleanField(default=False)
    ceated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 
    updated_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE) 

    def save(self, *args, **kwargs):
        if not self.updated_at:
            self.updated_at = datetime.datetime.now()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
