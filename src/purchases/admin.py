from django.contrib import admin

# Register your models here.
from purchases.models import PurchaseDocumentDefinition, PurchaseItem, PurchaseItemExternalNames, PurchaseDocument, \
    PurchaseDocumentPosition

admin.site.register(PurchaseDocumentDefinition)
admin.site.register(PurchaseItem)
admin.site.register(PurchaseItemExternalNames)
admin.site.register(PurchaseDocument)
admin.site.register(PurchaseDocumentPosition)