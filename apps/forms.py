from django import forms
from .models import Post
from django import forms
from .models import Blog, Blog_category, Product, ProductCategory
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class BlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        Blog_category.objects.all(),
        to_field_name='id',
        empty_label=None,
        required=True
    )

    class Meta:
        model = Blog
        exclude = ('created_at',)


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        ProductCategory.objects.all(),
        to_field_name='id',
        empty_label=None,
        required=True
    )

    class Meta:
        model = Blog
        exclude = ('content',)
