import datetime

from utils import run_shell_command
from settings import PROJECT_DIRS, DESTINATION_DIR, PROJECT_ARCNAME_TAIL




def backup_dirs():
    dir_params = {'project_dirs': ' '.join(x for x in PROJECT_DIRS),
                  'dest_dir': DESTINATION_DIR,
                  'arch_file_tail': PROJECT_ARCNAME_TAIL,
                  'dt': datetime.datetime.now().strftime('%Y%m%d_%H%M%S'),
                 }
    command = 'tar -zcf {dest_dir}/{dt}{arch_file_tail} {project_dirs}'.format(**dir_params)
    run_shell_command(command=command)