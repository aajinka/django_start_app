from django import forms
from .models import Article, Category, Comment

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class CreateArticle(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ["title","year","slug","category","body","thumb","author"]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zadej název inovace'}),
            #'year': forms.IntegerField(attrs={'class':'form-control'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            #'thumb': forms.ImageField(required=False),
            #'author': forms.Select(attrs={'class':'form-control'}),  
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', "id":"inovation", "type":"hidden"}),
            'category': forms.Select(choices = choice_list, attrs={'class':'form-control'}),
        }
       
class EditArticle(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ["title","year","slug","category","body","thumb"]
        widgets = {
            'category': forms.Select(choices = choice_list, attrs={'class':'form-control'}),
        }

class CommentArticle(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ['name', 'body']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
