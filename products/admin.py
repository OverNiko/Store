from django.contrib import admin

from products.models import ProductCategory, Product, Basket


admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category') # Показывает поля в таблице
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category') # Меняет поля внутри таблицы
    readonly_fields = ('description', ) # Запрещает редактировать поля внутри таблицы
    ordering = ('name',) # По умолчанию сортирует от А до Я
    search_fields = ('name',) # Поиск по имени
    
    
class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'create_timestamp')
    readonly_fields = ('product', 'create_timestamp',)
    extra = 1 # Добавляет возможность добавления продуктов внутри таблицы за админа