from django.db import models as m

class UserInfo(m.Model):                    #созд база с 2мя колонками
    name = m.TextField(unique=True)         #нельзя пустую колонку, и будет еще уникальна
    greeting = m.TextField(null=True, blank=True)       #тип чтобы были доступны пустые стоки

    class Meta:
        verbose_name_plural = "User Info"

    def __str__(self):
        return f"UserInfo(id={self.pk},name={self.name!r})"
