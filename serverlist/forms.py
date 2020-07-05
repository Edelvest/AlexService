from django import forms
from django.forms import inlineformset_factory

from .models import *


class ServerCreationForm(forms.ModelForm):
    class Meta:
        model = Server
        fields = ['name', 'description', 'server_type', 'cpu', 'ram']


class IpCreationForm(forms.ModelForm):
    class Meta:
        model = ServerIP
        fields = ['ip']

    def __init__(self, *args, **kwargs):
        super(IpCreationForm, self).__init__(*args, **kwargs)
        self.fields['ip'].widget.attrs['placeholder'] = 'Enter ip'


ServerIpFormSet = inlineformset_factory(Server, ServerIP, form=IpCreationForm)
