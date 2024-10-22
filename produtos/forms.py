from django import forms
from produtos.models import Categoria, Produto


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome': 'Nome da categoria',
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'categoria', 'imagem']
        labels = {
            'nome': 'Nome do Produto',
            'preco': 'Preço(R$)',
            'categoria': 'Categoria',
            'imagem': 'Imagem',
        }     