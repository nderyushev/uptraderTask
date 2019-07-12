from django.contrib import admin
from menu_app.models import MenuItem
from menu_app.forms import MenuItemForm


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    form = MenuItemForm


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    form = MenuItemForm

admin.site.register(
    MenuItem, 
    MenuItemAdmin
)