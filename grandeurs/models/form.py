from django     import forms
from .grandeur  import Grandeur


class GrandeurForm(forms.ModelForm):
    class Meta: 
        model = Grandeur
        fields = '__all__'
        widgets = {
            'nom':          forms.TextInput(attrs = {'class': 'form-control'}),
            'unite':        forms.TextInput(attrs = {'class': 'form-control'}),
            'valeurMin':    forms.NumberInput(attrs = {'class': 'form-control'}),
            'valeurMax':    forms.NumberInput(attrs = {'class': 'form-control'}),
        }

        def clean(self):
            cleaned_data = super().clean()
            valeur_min = cleaned_data.get('valeurMin')
            valeur_max = cleaned_data.get('valeurMax')

            if valeur_min is not None and valeur_max is not None and valeur_min >= valeur_max:
                raise forms.ValidationError('The minimum value must be less than the maximum value.')
            
            return cleaned_data