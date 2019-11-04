from django.forms import ModelForm

from .models import Day


class DayCreateForm(ModelForm):
    class Meta:
        model = Day
        # fields = '__all__'  # 特定のフィールドを指定したい場合はタップルで表記
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'placeholder': 'This area is not required.\
             And you can take some notes'
        })
