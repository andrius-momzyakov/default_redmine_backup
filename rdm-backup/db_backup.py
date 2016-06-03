import datetime

from utils import run_shell_command
from settings import DATABASE as DB
from settings import DB_ARCNAME_TAIL
from settings import DESTINATION_DIR


def backup_db():
    db_params = {'db': DB['pg_dbname'],
                 'user': DB['pg_user'],
                 'host': DB['pg_host'],
                 'port': DB['pg_port'],
                 'dt': datetime.datetime.now().strftime('%Y%m%d_%H%M%S'),
                 'arch_file_tail': DB_ARCNAME_TAIL,
                 'dest': DESTINATION_DIR}
    command = 'pg_dump -d {db} -U {user} -w -h {host} -p {port} -F tar -f {dest}/{dt}{arch_file_tail}'.format(**db_params)
    run_shell_command(command=command)
