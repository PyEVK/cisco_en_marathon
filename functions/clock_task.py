import re


def clock_task(ssh):
    config_commands = [
        "clock timezone GMT +0",
    ]

    regex = re.compile(r"(.+),.+")

    ssh.send_config_set(config_commands)

    cmd_output = ssh.send_command('show ntp status')

    match = regex.match(cmd_output)

    if match:
        return "Clock is sync"
    else:
        return "Clock is unsync"
