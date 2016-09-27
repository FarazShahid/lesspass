import json

from api import models


def create_password_with(entry):
    settings = json.dumps(entry.password.settings)
    lowercase = 'lowercase' in settings
    uppercase = 'uppercase' in settings
    symbols = 'symbols' in settings
    numbers = 'numbers' in settings
    user = models.LessPassUser.objects.get(id=entry.user.id)
    models.Password.objects.create(id=entry.id, site=entry.site, login=entry.login, user=user,
                                   lowercase=lowercase, uppercase=uppercase, symbols=symbols, numbers=numbers,
                                   counter=entry.password.counter, length=entry.password.length)
