from .models import Entry

class Meta(type):
    def __getitem__(self, key):
        try:
            entry = Entry.objects.get(key=key, enabled=True)
        except Entry.DoesNotExist as e:
            raise KeyError(key) from e

        if entry.type == Entry.Types.STRING:
            return entry.value
        elif entry.type == Entry.Types.INTEGER:
            return int(entry.value)
        elif entry.type == Entry.Types.FLOAT:
            return float(entry.value)

        raise TypeError

    def __setitem__(self, key, value):
        if value is None:
            raise ValueError('Cannot set registry value to None')

        try:
            entry = Entry.objects.get(key=key)
        except Entry.DoesNotExist:
            entry = Entry(key=key)

        entry.value = value

        if type(value) == int:
            entry.type = Entry.Types.INTEGER
        elif type(value) == float:
            entry.type = Entry.Types.FLOAT
        else:
            entry.type = Entry.Types.STRING

        entry.enabled = True
        entry.save()

    def __delitem__(self, key):
        try:
            entry = Entry.objects.get(key=key)
        except Entry.DoesNotExist as e:
            raise KeyError(key) from e

        entry.delete()

    def __iter__(self):
        return iter(Entry.objects.filter(enabled=True))

    def __contains__(self, key):
        return Entry.objects.filter(key=key).count() > 0


class reg(metaclass=Meta):
    @classmethod
    def get(cls, key, default=None):
        try:
            return cls[key]
        except Entry.DoesNotExist:
            return default
