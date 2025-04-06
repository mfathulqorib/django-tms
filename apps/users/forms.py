from django import forms
from django.contrib.auth.models import User

from apps.warehouses.models import Warehouse

from .models import ProfileUser


class ProfileForm(forms.ModelForm):
    warehouse = forms.ModelChoiceField(
        queryset=Warehouse.objects.all(),
        required=True,
        label="warehouse location",
    )

    class Meta:
        model = ProfileUser
        fields = ["name", "warehouse"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": "w-full px-4 py-2 border rounded-md focus:ring focus:ring-blue-300"
                }
            )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "class": "w-full px-4 py-2 border rounded-md focus:ring focus:ring-blue-300"
                }
            )
