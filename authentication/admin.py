from django.contrib import admin
from authentication.models import User, Client, Org

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Org)
