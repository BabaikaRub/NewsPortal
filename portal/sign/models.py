from django.db import models
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


# Скрипт для автомтического добавлния нового пользователя в группу common
class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)

        return user

