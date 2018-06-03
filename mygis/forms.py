from django.forms import ModelForm
from mygis.models import *

# create the form class
class PriceForm(ModelForm):
    class Meta:
        model = Mysite_PriceTask
        fields = ('message_person_id','food_id','market_id','data_time','price') 