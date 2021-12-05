# from django import forms
# from mainapp.models import Product, ProductCategory
#
#
# class ProductProfileForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name', 'price', 'image', 'category', 'description', 'short_description', 'active')
#
#     def __init__(self, *args, **kwargs):
#         super(ProductProfileForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs['readonly'] = True
#         self.fields['price'].widget.attrs['readonly'] = True
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control py-4'
#         self.fields['image'].widget.attrs['class'] = 'custom-file-input'
#
#
# class CategoryProfileForm(forms.ModelForm):
#     class Meta:
#         model = ProductCategory
#         fields = ('name' , 'description', 'is_active')
#
#     def __init__(self, *args, **kwargs):
#         super(CategoryProfileForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'