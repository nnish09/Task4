from django import forms
from client.models import Client
from django.forms import ModelForm
from django.conf import settings


class ClientForm(forms.ModelForm):
    client_name = forms.CharField(max_length=60,required=True)
    email = forms.EmailField(max_length=100,required=True)
    contact_name = forms.CharField(max_length=60)
    street_name=forms.CharField()
    suburb=forms.CharField()
    postcode=forms.CharField(max_length=10)
    state=forms.CharField(max_length=200)
    phone_no = forms.CharField( max_length=10,required=True) 

   
    class Meta:
        model = Client
        fields = ('client_name',  'email', 'contact_name','street_name','suburb','state','postcode','phone_no',)
        

    def clean_client_name(self):
        client_name = self.cleaned_data.get('client_name')
        if client_name and Client.objects.filter(client_name=client_name).count() > 0:
            raise forms.ValidationError('This client name is already registered.')
        return client_name

    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # username = self.cleaned_data.get('username')
        if email and Client.objects.filter(email=email).count() > 0:
            raise forms.ValidationError('This email address is already registered.')
        return email

    

class UpdateProfile(forms.ModelForm):
    client_name = forms.CharField(max_length=60,required=True)
    email = forms.EmailField(max_length=100,required=True)
    contact_name = forms.CharField(max_length=60)
    street_name=forms.CharField()
    suburb=forms.CharField()
    postcode=forms.CharField(max_length=10)
    state=forms.CharField(max_length=200)
    phone_no = forms.CharField( max_length=10,required=True) 

   
    class Meta:
        model = Client
        fields = ('client_name',  'email', 'contact_name','street_name','suburb','state','postcode','phone_no',)
        

    def __init__(self, *args, **kwargs):
       super(UpdateProfile, self).__init__(*args, **kwargs)
       self.fields['client_name'].widget.attrs['readonly'] = True


    