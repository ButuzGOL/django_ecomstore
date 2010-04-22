from django import forms
from ecomstore.catalog.models import Product, ProductReview

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
    
    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return self.cleaned_data['price']

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        exclude = ('user', 'product', 'is_approved')
