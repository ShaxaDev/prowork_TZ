from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account,Territory
from .forms import RegistrationForm,CustomUserChangeForm


class AccountAdmin(UserAdmin):
	add_form=RegistrationForm
	form=CustomUserChangeForm
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = (
		('Personal', {'fields': ('username','email', 'password','phone_number','territory')}),
		('Permissions', {'fields': ('is_staff', 'is_active',)}),
    )
	add_fieldsets = ( (None, {
		'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','phone_number')}
        ),
    )

admin.site.register(Account, AccountAdmin)
admin.site.register(Territory)
