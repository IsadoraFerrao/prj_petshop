from django import forms
from reserva.models import Reserva
from datetime import date

class ReservaForm(forms.ModelForm):

    def clean_date(self):
        form_date = self.cleaned_data["data"]
        today_date = date.today()
        if form_date < today_date:
            raise forms.ValidationError('OPS, a data informada é anterior a data de hoje')
        return form_date

    def clean_shift(self):
        form_date = self.cleaned_data["data"]
        form_shift = self.cleaned_data["shift"]
        baths_in_same_day_and_hour = Reserva.objects.filter(data=form_date, shift=form_shift).count()
        if baths_in_same_day_and_hour >= 4:
            raise forms.ValidationError(f'Ops esse horário já esta lotado, para o turno da {form_shift}')
        return form_shift
        

    """ def clean_date(self):
        reserva = Reserva.objects.filter(data__day=16).count()
        if reserva >= 4:
            raise forms.ValidationError('Não temos mais vagas para esta data!')
        return 
 """

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data', 'turno',
             'tamanho', 'observacoes'
        ]
