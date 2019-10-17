from django.forms import ModelForm, Textarea

from .models import Day


class DayCreateForm(ModelForm):
    class Meta:
        model = Day
        widgets = {'parameters': Textarea(attrs={'cols': 35, 'rows': 6})}
        fields = '__all__'  # 特定のフィールドを指定したい場合はタップルで表記
