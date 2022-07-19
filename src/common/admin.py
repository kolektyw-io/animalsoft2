from django.contrib import admin

# Register your models here.
from common.models import ItemType, ItemCategory, CommonItem, CommonItemBarcode, Contractor, Currency, Branch

admin.site.register(ItemType)
admin.site.register(ItemCategory)
admin.site.register(CommonItem)
admin.site.register(CommonItemBarcode)
admin.site.register(Contractor)
admin.site.register(Currency)
admin.site.register(Branch)