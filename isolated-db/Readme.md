==========================================================================================
py .\manage.py makemigrations polls [App Name : polls]
------------------------------------------------------------------------------------------
Makemigrations for default configuration.
py .\manage.py makemigrations polls
py .\manage.py migrate

------------------------------------------------------------------------------------------
[ database name only work with tenant_context_manage for makemigrations ]
[ database name only work with manage.py for migrate not work 'tenant_context_manage' ]

python tenant_context_manage.py thor makemigrations
py .\manage.py migrate --database=thor     [For migrate 'thor' database]
py .\manage.py migrate   [For default user migrate]

-----------------------------------------/ Create Super User \----------------------------
------------------------------------------------------------------------------------------
python .\manage.py createsuperuser
python tenant_context_manage.py thor createsuperuser --database=thor
==========================================================================================
Database Migration: NOt Find solution for load data.
    Error! : sqlite3.ProgrammingError: Cannot operate on a closed database.
    python -Xutf8 manage.py dumpdata --database=default > default_data.json
==========================================================================================


To make migrations and migrate we have to use different manage.py

python tenant_context_manage.py thor createsuperuser --database=thor

python tenant_context_manage.py default makemigrations

python tenant_context_manage.py thor makemigrations
python tenant_context_manage.py potter makemigrations

python tenant_context_manage.py default migrate

And check if the table exists or not in the database using DB Viewer.