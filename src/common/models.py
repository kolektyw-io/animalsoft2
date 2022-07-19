from django.db import models


# Create your models here.

class ItemType(models.Model):
    name = models.TextField()
    supports_stocking = models.BooleanField(default=False)


class ItemCategory(models.Model):
    name = models.TextField()
    parent = models.ForeignKey(
        "ItemCategory",
        null=True,
        on_delete=models.deletion.SET_NULL
    )


class CommonItem(models.Model):
    name = models.TextField(null=False, blank=False)
    SKU = models.TextField()
    category = models.ForeignKey(
        ItemCategory,
        on_delete=models.deletion.SET_NULL,
        null=True
    )

