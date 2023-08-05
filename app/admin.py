from django.contrib import admin
from . models import Category, Product, Employee

# admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display =['name','id']
    search_fields =['name']
    list_filter=['id']
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display =['name','price']
admin.site.register(Product, ProductAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display =['name','email','address','phone']
admin.site.register(Employee, EmployeeAdmin)
    