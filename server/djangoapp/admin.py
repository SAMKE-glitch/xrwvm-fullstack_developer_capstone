#from django.contrib import admin
#from .models import related models
from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
# Optional: CarModelInline class to include in CarMakeAdmin
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

# Optional: CarModelAdmin class to customize the CarModel display
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'mileage')

# Optional: CarMakeAdmin class to include CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')

# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
