import subprocess


def run_shell_command(command):
    print('Running:')
    print(command)
    command_parsed = command.split()
    res = subprocess.run(command_parsed, universal_newlines=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    if res.returncode !=0:
        print('Error: ' + str(res.stderr))
    else:
        print(str(res.stdout))
