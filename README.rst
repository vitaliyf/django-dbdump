-------------
django-dbdump
-------------

This tiny Django application provides a "dbdump" management command that wraps
mysqldump or pg_dump and allows you to create SQL dumps of your configured
databases.

To use, add 'dbdump' to your INSTALLED_APPS.

Usage:

`$ manage.py dbdump`
`$ manage.py dbdump --db-name=mydb --debug --compress=gzip`

You can dump only table schema without data or exclude tables completely
using DB_DUMP_EMPTY_TABLES and DB_DUMP_EXCLUDED_TABLES settings inside
your settings.DATABASES definition. For example::

    DATABASES = {
        'default': {
            'ENGINE': 'mysql',
            ...
            'DB_DUMP_EMPTY_TABLES': ['table1', 'table2'],
        }
    }

will not include contents of table1 and table2 in your output.

See http://github.com/vitaliyf/django-dbdump for more information.