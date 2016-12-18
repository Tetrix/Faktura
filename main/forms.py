from django import forms
from main.models import Article, Import, PackingList, Export


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('fabric', 'color', 'supplier')

class ImportForm(forms.ModelForm):
    add_packing_list = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Import
        fields = ('article','quantity', 'comment')

class PackingListForm(forms.ModelForm):
    class Meta:
        model = PackingList
        fields = ('name','date')


class ExportForm(forms.ModelForm):
    add_packing_list = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Export
        fields = ('article','order', 'art', 'use', 'comment')
