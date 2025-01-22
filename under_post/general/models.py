from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models


class Order(models.Model):
    index = models.AutoField(primary_key=True, editable=False, verbose_name=_('Index'))
    full_name = models.CharField(max_length=100, verbose_name=_('Full name'), blank=True, null=True)
    phone = models.CharField(max_length=12, verbose_name=_('Phone number'), null=True, blank=True)
    email = models.EmailField(max_length=120, verbose_name=_('Email'), null=True, blank=True)
    message = models.TextField(verbose_name=_('Message'), null=True, blank=True)

    class Meta:
        db_table = 'orders'
        verbose_name = _('Orders')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return f"{self.index}. {self.phone}/{self.email}"
