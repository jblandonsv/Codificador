from django import forms

import autocomplete_light
from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from codificador.models import Unidad,Archivo,folio

#Formulario de Registro de Archivos
class ArchivoForm(ModelForm):
	class Meta:
		model = Archivo

#Inlines Formsets
FoliosFormset = inlineformset_factory(Archivo, folio)

class LoginForm(forms.Form):
	username = forms.CharField(label=u'Usuario:')
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class ArchivoForm(forms.ModelForm):
    unidad_responsable = forms.ModelChoiceField(Unidad.objects.all(),
        widget=autocomplete_light.ChoiceWidget('Unidades'))

    class Meta:
        model = Archivo