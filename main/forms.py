from django import forms
from .models import Blog, Comment


class ReviewForm(forms.Form):

    name = forms.CharField(
        label='Ваше имя',
        max_length=50,
        min_length=2
    )

    rating = forms.ChoiceField(
        label='Как вы оцениваете сайт?',
        choices=[
            (5, 'Отлично'),
            (4, 'Хорошо'),
            (3, 'Удовлетворительно'),
            (2, 'Плохо')
        ],
        widget=forms.RadioSelect
    )

    frequency = forms.ChoiceField(
        label='Как часто вы посещаете сайт?',
        choices=[
            ('daily', 'Каждый день'),
            ('weekly', 'Несколько раз в неделю'),
            ('rarely', 'Редко')
        ]
    )

    liked = forms.MultipleChoiceField(
        label='Что вам понравилось?',
        choices=[
            ('design', 'Оформление сайта'),
            ('information', 'Информация об игре'),
            ('resources', 'Полезные ресурсы'),
            ('navigation', 'Удобство навигации')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    wishes = forms.CharField(
        label='Ваши пожелания и замечания',
        widget=forms.Textarea,
        min_length=5,
        max_length=500,
        required=False
    )



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Ваш комментарий'
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4})
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'short_content', 'content', 'pub_date', 'image']
        labels = {
            'title': 'Заголовок',
            'short_content': 'Краткое содержание',
            'content': 'Полное содержание',
            'pub_date': 'Дата публикации',
            'image': 'Изображение статьи'
        }
        widgets = {
            'pub_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'}
            ),
            'short_content': forms.Textarea(attrs={'rows': 3}),
            'content': forms.Textarea(attrs={'rows': 8})
        }