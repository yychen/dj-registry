# DJ-Registry
This is a simple, easy access key-value registry for Django. Sometimes you would like to have some flexibility in your settings.
Putting your settings in `settings.py` or as environment variables also mean an Engineer familiar with code or command line is required to alter them.

This Django app leverage the built-in Django admin so changing settings is easier as you can use the web interface.

## Installation

Install DJ-Registry with your favorite Python package manager:

```
pip install dj_registry
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
./manage.py migrate
```

Then, we're all set!

## Usage

