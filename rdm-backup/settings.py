# Redmine project database
DATABASE = {'pg_dbname': 'redmine_default',
            'pg_user': 'postgres',
            'pg_host': '127.0.0.1',
            'pg_port': 5432,
            }

DB_ARCNAME_TAIL = '_db_taskman.bakup.tar'


# A list of project paths of a "/var/lib/redmine/default" style
PROJECT_DIRS = ('/var/lib/redmine/default', '/etc/redmine/default')

PROJECT_ARCNAME_TAIL = '_redmine_project.backup.tar.gz'

DESTINATION_DIR = '/somedir'

