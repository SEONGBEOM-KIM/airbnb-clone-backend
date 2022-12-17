from django.db import models


class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(
        auto_now_add=True,  # When Created
    )
    updated_at = models.DateTimeField(
        auto_now=True,  # When Updated
    )

    # Django do not input this model to database
    class Meta:
        abstract = True
