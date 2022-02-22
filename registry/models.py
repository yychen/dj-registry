from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class Entry(models.Model):
    class Types:
        STRING = 'str'
        INTEGER = 'int'
        FLOAT = 'float'
        BOOLEAN = 'bool'

        choices = (
            (STRING, 'string'),
            (INTEGER, 'integer'),
            (FLOAT, 'float'),
            (BOOLEAN, 'bool'),
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
            elif self.type == self.Types.BOOLEAN:
                if self.value.lower() in ['true', 'yes', '1']:
                    self.value = 'true'

                if self.value.lower() in ['false', 'no', '0']:
                    self.value = 'false'

                if self.value != 'true' and self.value != 'false':
                    raise ValidationError({'value': _('Accepted boolean values: true, false, yes, no, 0, 1')})

        except ValueError:
            raise ValidationError({'value': _('Invalid value of the specified type.')})

    class Meta:
        verbose_name_plural = 'entries'
