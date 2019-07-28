
from django import forms
from .models import Users
class DemoForm(forms.Form):
    name = forms.CharField(max_length=100)
    email =forms.EmailField()
    password =forms.CharField(max_length=20,widget=forms.PasswordInput())
    mobile =forms.IntegerField()

    color =forms.CharField(max_length=20,
                           label="my Color",
                           widget=forms.TextInput(
                               attrs={
                                    'type':'color',
                                   'placeholder':'Color',
                                   'class':'class1',
                                   'id':'input-id',
                                   'style':'width:100px;'

                               }
                           )
                           )
    message=forms.CharField(
        widget=forms.Textarea()
    )
    select_gender=(
        ('', '--Select gender--'),
        ('male','Male'),
        ('female', 'FeMale'),
    )
    gender= forms.ChoiceField(choices=select_gender)



class Userform(forms.ModelForm):
    class Meta:
        model = Users
        fields =('__all__')
        # fields =()