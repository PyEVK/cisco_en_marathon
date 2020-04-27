from functions.save_config import save_config
from functions.check_cdp_enabled import check_cdp_enabled
from functions.get_version_data import get_version_data
from functions.clock_task import clock_task
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException


def home_task(device, backup_dir):
    result = []
    try:
        with ConnectHandler(**device) as ssh:
            ssh.enable()
            host_name = ssh.find_prompt()[:-1]
            result.append(host_name)

            result += get_version_data(ssh)

            save_config(ssh, host_name, backup_dir)

            result.append(check_cdp_enabled(ssh))

            result.append(clock_task(ssh))

            return '|'.join(result)

    except (NetMikoAuthenticationException, NetMikoTimeoutException) as e:
        return "Connection error: " + str(e)
