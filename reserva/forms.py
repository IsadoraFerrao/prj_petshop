from django import forms
from reserva.models import Reserva

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno', 'tamanho', 'observacoes'
        ]