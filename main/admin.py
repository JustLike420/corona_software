from django.contrib import admin
from .models import Posts
from django import forms
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(label='Системные требования', widget=CKEditorWidget())
    details = forms.CharField(label='Описание', widget=CKEditorWidget())

    class Meta:
        model = Posts
        fields = '__all__'


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    form = PostAdminForm


