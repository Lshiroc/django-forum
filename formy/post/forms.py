from django import forms

from .models import Post, Tag

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'context', 'tags',)

    INPUT_CLASS = 'w-full mb-4 p-2 border border-solid border-2 border-gray-100 outline-green-400 text-lg rounded-md'

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': INPUT_CLASS,
        'placeholder': 'Post title'
    }))
    context = forms.CharField(widget=forms.Textarea(attrs={
        'class': INPUT_CLASS,
        'placeholder': 'Post Context'
    }))
    tags = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'hidden',
        'id': 'hiddenfield'
    }))

