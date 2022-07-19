from django.db import models


# Create your models here.

class ItemType(models.Model):
    name = models.TextField()
    supports_stocking = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ItemCategory(models.Model):
    name = models.TextField()
    parent = models.ForeignKey(
        "ItemCategory",
        null=True,
        on_delete=models.deletion.SET_NULL
    )

    def __str__(self):
        return self.name


class CommonItem(models.Model):
    name = models.TextField(null=False, blank=False)
    SKU = models.TextField(null=True, blank=True)
    category = models.ForeignKey(
        ItemCategory,
        on_delete=models.deletion.SET_NULL,
        null=True, blank=True
    )
    type_of = models.ForeignKey(ItemType, null=True, on_delete=models.deletion.PROTECT)

    def __str__(self):
        return self.name


class CommonItemBarcode(models.Model):
    item = models.ForeignKey(CommonItem, on_delete=models.deletion.PROTECT)
    barcode = models.TextField()


class Contractor(models.Model):
    short_name = models.TextField()
    full_name = models.TextField(null=True)
    address = models.TextField()
    vat_number = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_vendor = models.BooleanField(default=True)
    is_recipient = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pk}, {self.short_name}"


class ContractorBranch(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.deletion.PROTECT)
    name = models.TextField()
    address = models.TextField()

    def __str__(self):
        return f"{self.contractor.name} / {self.name}"


class Currency(models.Model):
    name = models.TextField()
    symbol = models.TextField()

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.TextField()
    symbol = models.TextField()

    def __str__(self):
        return self.name
