from django.forms import ModelForm,  CharField, DateField, TextInput, DateInput, DateTimeField

from .models import Author


class AuthorForm(ModelForm):
    fullname = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    born_date = DateField(widget=DateInput(attrs={"class": "form-control"}))
    born_location = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))
    description = CharField(max_length=100, widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description",]
