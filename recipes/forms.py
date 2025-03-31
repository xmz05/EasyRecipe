from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'ingredients',
            'instructions',
            'category',
            'cooking_time',
            'calories'
        ]

        widgets = {
            'ingredients': forms.Textarea(attrs={'rows':3}),
            'instructions': forms.Textarea(attrs={'rows': 5}),
        }