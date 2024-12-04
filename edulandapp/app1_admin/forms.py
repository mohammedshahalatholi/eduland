from django.forms import ModelForm
from .models import Mainpage
class AForm(ModelForm):
    class Meta:
        model = Mainpage
        fields = ("__all__")

    