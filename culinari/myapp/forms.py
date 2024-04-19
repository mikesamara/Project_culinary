

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


from .models import Recipe, Category

User = get_user_model()
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'







class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = '__all__'






class UserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        max_length=254,
        widget=forms.EmailInput(attrs={'placeholder': 'Адрес электронной почты'})
    )

    password1 = forms.CharField(
        label='Password',
        min_length=8,
        widget=forms.PasswordInput(attrs={'placeholder': 'пароль'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']