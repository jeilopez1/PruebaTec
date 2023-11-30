from django.contrib import admin
from django.apps import apps
from .models import PaymentReference  

class MiModeloAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Operadores').exists():  # Si el usuario pertenece al grupo 'Operadores'
            return [f.name for f in self.model._meta.fields if f.name != 'value']  # Todos los campos son de solo lectura excepto 'value'
        return super().get_readonly_fields(request, obj)

# Obtén todos los modelos de tu aplicación "PracticasAcademicas"
app_models = apps.get_app_config('pay').get_models()

# Registra todos los modelos en el administrador de Django
for model in app_models:
    if model == PaymentReference:
        admin.site.register(model, MiModeloAdmin)  # Registra tu modelo con la nueva configuración de administrador
    else:
        admin.site.register(model)
