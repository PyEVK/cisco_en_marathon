import re
import time


def clock_task(ssh, ntp_server):
    config_commands = [
        "clock timezone GMT +0",
    ]

    if check_ntp_avail(ssh, ntp_server):
        config_commands.append("ntp server " + ntp_server + " prefer")

    regex = re.compile(r"Clock is synchronized,.+")

    ssh.send_config_set(config_commands)

    time.sleep(5)

    cmd_output = ssh.send_command('show ntp status')

    match = regex.search(cmd_output)

    if match:
        return "Clock is sync"
    else:
        return "Clock is unsync"


def check_ntp_avail(ssh, ntp_server):
    cmd_output = ssh.send_command("ping " + ntp_server)
    regex = re.compile(r"Success rate is (\d+) percent")

    match = regex.search(cmd_output)
    rate = 0
    if match:
        rate = int(match.group(1))

    return rate > 0
