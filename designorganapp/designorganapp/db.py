import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Base de Datos sqlite3
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# psycopg2

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_design',
        'USER':'',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'5433',
    }
}

# Base de Datos sqlite3
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
