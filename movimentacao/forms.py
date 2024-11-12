from movimentacao.models import Movimentacao
from produtos import forms


class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['produto','quantidade', 'tipo']