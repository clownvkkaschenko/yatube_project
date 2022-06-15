from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text', 'image')
        labels = {
            'text': 'Пишите что-нибудь приятное, пожалуйста ^-^',
            'group': 'Выберите группу',
        }
        help_texts = {
            'text': 'Текст вашего поста',
            'group': 'Группа, к которой будет относиться пост',
            'image': 'Ваше изображение будет показано в разрешении 1280x420'
        }
