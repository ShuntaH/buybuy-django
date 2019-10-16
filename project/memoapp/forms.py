from django import forms

from .models import Day


class DayCreateForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = '__all__'  # 特定のフィールドを指定したい場合はタップルで表記
