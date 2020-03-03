from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreateForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
	form = UserAdminChangeForm
	add_form = UserAdminChangeForm

	list_display = ('email','admin')
	list_filter = ('admin','staff','active')

	fieldsets = (
		(None,{'fields':('email','password')}),
		('personal info', {'fields':()}),
		('Permissions',{'fields':('admin',)}),
	)

	add_fieldsets = (
		(None, {
			'classes':('wide',),
			'fields': ('email','password1','password2')}
			),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(User, UserAdmin) 

admin.site.unregister(Group)



