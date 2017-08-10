from django.forms import ModelForm
from myapp.models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ("i_name","i_host","i_service","i_link_source","i_subsystem","i_processName","i_baseDir")