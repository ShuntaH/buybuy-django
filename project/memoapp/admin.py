from django.contrib import admin
from .forms import DayCreateForm
from .models import Day

# Register your models here.
admin.site.register(Day)


class DayCreateAdmin(admin.ModelAdmin):
    form = DayCreateForm
