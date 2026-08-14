from django.contrib.auth.models import AbstractUser
from django.db import models


# Account model
class User(AbstractUser):

    # User role
    class Role(models.TextChoices):
        LEARNER = "LEARNER", "Learner"
        ADMINISTRATOR = "ADMINISTRATOR", "Administrator"

    # User properties
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.LEARNER,
    )

    # Maximum number of documents
    document_quota = models.PositiveIntegerField(default=10)

    # Maximum storage capacity in MB
    storage_quota_mb = models.PositiveIntegerField(default=500)

    def __str__(self):
        return f"{self.username} ({self.role})"