from django import forms
from .models import Property, Booking

class PropertySearchForm(forms.Form):
    property_type = forms.ChoiceField(
        choices=[('', 'All Types')] + list(Property.PROPERTY_TYPES),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    listing_type = forms.ChoiceField(
        choices=[('', 'All Listings')] + list(Property.LISTING_TYPES),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    min_price = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Min Price'
        })
    )
    max_price = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Max Price'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        min_price = cleaned_data.get('min_price')
        max_price = cleaned_data.get('max_price')
        
        if min_price and max_price and min_price > max_price:
            raise forms.ValidationError('Minimum price cannot be greater than maximum price.')
        
        return cleaned_data

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['move_in_date', 'duration_months']
        widgets = {
            'move_in_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'duration_months': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'max': '24'
            })
        }

    def clean_duration_months(self):
        duration = self.cleaned_data.get('duration_months')
        if duration < 1 or duration > 24:
            raise forms.ValidationError('Duration must be between 1 and 24 months.')
        return duration 