from django.contrib import admin
from grid import forms
from grid.models import Employer


class EmployerAdminForm(forms.EmployerForm):
    class Meta:
        model = Employer
        fields = '__all__'


class EmployerAdmin(admin.ModelAdmin):
    form = EmployerAdminForm
    list_display = ('name', 'email', 'contact')
    # list_display_links = ('id', 'name')
    # search_fields = ('id', 'name')

admin.site.register(Employer, EmployerAdmin)
