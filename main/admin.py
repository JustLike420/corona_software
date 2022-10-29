from django.contrib import admin
from .models import Posts
from django import forms
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(label='Системные требования', widget=CKEditorWidget(), initial='<b>RAB: </b><br>'
                                                                                                 '<b>CPU: </b>-<br>'
                                                                                                 '<b>OS: </b>Windows 7 or newer<br>'
                                                                                                 '<b>SOUND CARD: </b>DirectX Compatible<br>'
                                                                                                 '<b>DEDICATED VIDEO RAM: </b>256 MB<br>')

    class Meta:
        model = Posts
        fields = '__all__'


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    list_filter = ('category',)
    form = PostAdminForm
