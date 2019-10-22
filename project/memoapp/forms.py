from django.forms import ModelForm, Textarea, TextInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Day


class DayCreateForm(ModelForm):
    class Meta:
        model = Day
        fields = '__all__'  # 特定のフィールドを指定したい場合はタップルで表記

    def __init__(self, *args, **kwargs):
        super(DayCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Added'))
        self.fields['text'].widget.attrs.update({
            'placeholder': 'You can take some notes'
        })


