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

    def clean_date(self):
        reserva = self.cleaned_data['data']
        if reserva.count() >= 14:
            raise forms.ValidationError('Não temos mais vagas para esta data!')
        else:
            return reserva

    """ def clean_date(self):
        reserva = Reserva.objects.filter(data__day=16).count()
        if reserva >= 4:
            raise forms.ValidationError('Não temos mais vagas para esta data!')
        return  """
 

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno',
             'tamanho', 'observacoes'
        ]