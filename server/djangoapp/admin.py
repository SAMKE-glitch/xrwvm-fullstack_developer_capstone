from django.contrib import admin
from .models import CarMake, CarModel

# Register your models here.


# Define CarModelInline class to include in CarMakeAdmin
class CarModelInline(admin.StackedInline):
    model = CarModel
    # Display 5 empty forms for adding CarModel 
    # instances under each CarMake
    extra = 5

# Define CarModelAdmin class to customize the CarModel display
class CarModelAdmin(admin.ModelAdmin):
    # Include 'mileage' field in list_display
    list_display = ('name', 'car_make', 'type', 'year', 'mileage')  


# Define CarMakeAdmin class to include CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
