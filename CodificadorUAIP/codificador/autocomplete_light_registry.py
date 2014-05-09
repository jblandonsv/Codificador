import autocomplete_light

from codificador.models import Unidad,Dependencia

#autocomplete_light.register(Unidad, search_fields=('nombre',),
#    autocomplete_js_attributes={'placeholder': 'Unidad Administrativa ..'})

autocomplete_light.register(Unidad, search_fields=('nombre','abreviatura',),name='Unidades',
    autocomplete_js_attributes={'placeholder': 'Unidad Administrativa ..'})

#autocomplete_light.register(Dependencia, search_fields=('nombre','abreviatura'),
#    autocomplete_js_attributes={'placeholder': 'Dependencia ..'})


class AutocompleteUnidad(autocomplete_light.AutocompleteModelBase):
    autocomplete_js_attributes={'placeholder': 'Unidad Organizativa (opciones segun Dependencia)..'}

    search_fields=('nombre','abreviatura',)

    def choices_for_request(self):
        q = self.request.GET.get('q', '')
        dependencia_id = self.request.GET.get('dependencia_id', None)

        #choices = self.choices.all()
        choices = Unidad.objects.filter(dependencia=dependencia_id)

        if q:
            #choices = choices.filter(name_ascii__icontains=q)
            choices = choices.filter(nombre__icontains=q)

        if dependencia_id:
            choices = choices.filter(dependencia_id=dependencia_id)

        return self.order_choices(choices)[0:self.limit_choices]

autocomplete_light.register(Unidad, AutocompleteUnidad)