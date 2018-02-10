from django import forms
from .models import Encuesta

class EncuestaForm(forms.ModelForm):

	CHOICES=[('1',' '),
   	         ('2',' '),
   	         ('3',' '),
   	         ('4',' '),
   	         ('5',' ')]

	like = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(attrs={'class' : 'custom'}),choices=CHOICES,label='1. ¿Te gustan las características del equipo?')

	CHOICES2=[('6',' '),
   	         ('7',' '),
   	         ('8',' '),
   	         ('9',' '),
   	         ('10',' ')]   	         
	design = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=CHOICES2,label='2. ¿Cómo calificarías su diseño?')

	more_like = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows': 3, 'cols': 50}),label="3. ¿Qué es lo que más te gusta?")

	CHOICES3=[('11',' '),
   	         ('12',' '),
   	         ]
	price = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class' : 'custom2'}),choices=CHOICES3,label='4. ¿Qué te parece su precio? ($2,899.00)')

	class Meta:
		model = Encuesta
		fields= ['like','design','more_like','price']

