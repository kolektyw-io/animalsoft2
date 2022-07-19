from django.db import models

# Create your models here.
from common.models import CommonItem, Contractor, Currency, Branch, ContractorBranch


class PurchaseDocumentDefinition(models.Model):
    name = models.TextField()
    mnemonic = models.TextField()

    def __str__(self):
        return f"({self.mnemonic}) {self.name}"


class PurchaseItem(models.Model):
    item = models.ForeignKey(CommonItem, on_delete=models.deletion.PROTECT)

    def __str__(self):
        return self.item.name


class PurchaseItemExternalNames(models.Model):
    item = models.ForeignKey(PurchaseItem, on_delete=models.deletion.SET_NULL, null=True)
    external_source = models.TextField()
    external_sku = models.TextField()
    external_name = models.TextField()


class PurchaseDocument(models.Model):
    definition = models.ForeignKey(PurchaseDocumentDefinition, on_delete=models.deletion.PROTECT)
    create_date = models.DateField(auto_now_add=True)
    sale_date = models.DateField(null=True)
    receive_date = models.DateField(null=True)
    branch = models.ForeignKey(Branch, on_delete=models.deletion.SET_NULL, null=True)
    internal_number = models.TextField()
    external_number = models.TextField()
    contractor = models.ForeignKey(Contractor, on_delete=models.deletion.PROTECT)
    contractor_div = models.ForeignKey(ContractorBranch, on_delete=models.deletion.PROTECT, null=True, blank=True)
    is_committed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.internal_number} ({self.external_number})"


class PurchaseDocumentPosition(models.Model):
    document = models.ForeignKey(PurchaseDocument, on_delete=models.deletion.CASCADE)
    item = models.ForeignKey(PurchaseItem, on_delete=models.deletion.PROTECT, null=True)
    is_committed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    currency = models.ForeignKey(Currency, on_delete=models.deletion.PROTECT)
    amount = models.FloatField(default=1)
    net_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    vat_amount_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    gross_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    net_value = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    vat_amount_value = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    gross_value = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.document.internal_number}\\{self.item.item.name}"