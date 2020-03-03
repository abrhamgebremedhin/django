from django.contrib.auth.models import User
from .models import Storage,Request
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


class BloodFilter(django_filters.FilterSet):
    class Meta:
        model = Storage
        fields = ['bloodType', 'storgeArea' ]

class RequestFilter(django_filters.FilterSet):
    class Meta:
        model = Request
        fields = ['bookedBy', 'RequestedBlood' ]








      