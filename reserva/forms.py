from django import forms
from reserva.models import Reserva
from datetime import date

class ReservaForm(forms.ModelForm):

    def clean_data(self):
        data = self.cleaned_data['data']
        hoje = date.today()
        if data < hoje:
            raise forms.ValidationError('Não é possivel realizar uma reserva para o passado!')
        return data

    """ def clean_turno(self):
        reserva_tarde = Reserva.objects.filter(turno='tarde').count()
        quant_max = 10
        if reserva_tarde > quant_max:
            raise forms.ValidationError('Não temos mais vagas para esta data!')
        return reserva_tarde
 """

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno',
             'tamanho', 'observacoes'
        ]