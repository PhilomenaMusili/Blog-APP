# manage forms
from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','content', 'status','category','date_created','tags']

