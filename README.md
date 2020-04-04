# DJ-Registry
This is a simple, easy access key-value registry for Django. Sometimes you would like to have some flexibility in your settings.
Putting your settings in `settings.py` or as environment variables also mean an engineer familiar with code or command line is required to alter them.

This Django app leverage the built-in Django admin so changing settings is easier as you can use the web interface.

## Requirements
* Python 3
* Django >= 1.11

I only did a quick test with Python 3.6 on Django 1.11 and the latest Django, which is 2.2.6 at the time being.

## Installation

Install DJ-Registry with your favorite Python package manager:

```
(venv)$ pip install dj_registry
```

Add `registry` to your `INSTALLED_APPS` settings:

```py
INSTALLED_APPS = [
    # other apps...

    'registry',
]
```

Migrate the database

```
(venv)$ ./manage.py migrate
```

Then, we're all set!

## Usage

Log in to the admin, and create some keys under the **Django Registry** > **Entries** section. Let's say, we create `mailgun.key` and `mailgun.domain` with the corresponding `string` type and values.
We then create another entry with `game.max_score` as the key, `10000` as the value and `integer` as the type.

The following example shows you how to access them in code:

```py
from registry.helper import reg

key = reg['mailgun.key']            # the key that you set
domain = reg['mailgun.domain']      # the domain that you set

max_score = reg['game.max_score']   # 10000, it is returned as an int
```

You can also use `get` if you want to have a default and avoid exceptions if the key is not available (not enabled or does not exist)

```py
reg.get('game.levels', 10)          # return 10 if key not found or disabled
reg['game.levels']                  # KeyError if key not found or disabled
```

You can set or delete entry if you want
```py
reg['game.levels'] = 12             # Set game.levels to 12 (integer) and save
del reg['game.levels']              # Delete game.levels
```

## Enabled and comment field
If you want to disable a key, just toggle the `enabled` boolean in the admin interface. It would be treated as if the key didn't exist. This is something meant to be used in the admin interface.
If you want to manipulate this in the code, you will have to access the raw model like the following:

```py
from registry.models import Entry

e = Entry.objects.get('game.levels')
e.enabled = False
e.save()
```

The comment field is also meant to be used in the admin interface. It is a convenient cell for user to put comments regarding to the settings, something like the following:

```
50: average use case.
9999: maximum special case
```

## Types
`integer`, `float`, `string`, and `boolean` are the supported types for now.
