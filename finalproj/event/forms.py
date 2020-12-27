from django import forms
from .models import Event,Category


choices = Category.objects.all().values_list('name','name')

choices_list = []

for item in choices:
    choices_list.append(item)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name','organizer','thumbnail','category','venue','desc','available')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name of the Event'}),
            'organizer': forms.TextInput(attrs={'class': 'form-control','value':'', 'id': 'elder', 'type':'hidden'}),
            'thumbnail': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            #'datetime': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control', 'placeholder':'Choose Category'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'available': forms.TextInput(attrs={'class': 'form-control'}),
        }



class UpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name','thumbnail','category','venue','desc','available')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name of the Event'}),
            #'organizer': forms.Select(attrs={'class': 'form-control'}),
            'thumbnail': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'available': forms.TextInput(attrs={'class': 'form-control'}),
        }