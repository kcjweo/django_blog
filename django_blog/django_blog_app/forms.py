from django import forms
from django.forms import fields
from .models import Comment

class CommentCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.files.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Comment
        fields = ("name", "text")