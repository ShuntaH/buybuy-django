from django.contrib import admin
from .forms import DayCreateForm

# Register your models here.


class DayCreateAdmin(admin.ModelAdmin):
    form = DayCreateForm
