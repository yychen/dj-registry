from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Entry(models.Model):
    class Types:
        STRING = 'str'
        INTEGER = 'int'
        FLOAT = 'float'

        choices = (
            (STRING, 'string'),
            (INTEGER, 'integer'),
            (FLOAT, 'float'),
        )

    key = models.CharField('Key', max_length=64, db_index=True)
    value = models.CharField('Value', max_length=512, blank=True)
    type = models.CharField('Type', max_length=8, choices=Types.choices, blank=True, default=Types.STRING)
    enabled = models.BooleanField('Enabled', default=True)
    comment = models.TextField('Comment', blank=True)

    def __str__(self):
        return self.key

    def clean(self):
        try:
            if self.type == self.Types.INTEGER:
                int(self.value)
            elif self.type == self.Types.FLOAT:
                float(self.value)
        except ValueError:
            raise ValidationError({'value': _('Invalid value of the specified type.')})


    class Meta:
        verbose_name_plural = 'entries'
