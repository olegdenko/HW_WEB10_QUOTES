from django.forms import ModelForm, ImageField, CharField, FileInput, TextInput

from .models import Author


class AuthorForm(ModelForm):
    description = CharField(max_length=150, widget=TextInput(attrs={"class": "form-control"}))
    path = ImageField(widget=FileInput(attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ["description", "path"]
