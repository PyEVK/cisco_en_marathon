import re


def get_version_data(ssh):
    """
    Получение информации о типе и версии оборудования
    :param ssh:
    :return:
    """
    cmd_output = ssh.send_command('show version')

    regex = re.compile(
        r"Cisco IOS Software, .+ \((?P<os_type>.+)\),.+"
        r"|\S+ (?P<dev_type>\S+) .+ with \S+ bytes of memory"
    )

    result = {}

    for match in regex.finditer(cmd_output):
        os_type, dev_type = match.group("os_type", "dev_type")
        if os_type:
            result["os_type"] = os_type + ' '
        if dev_type:
            result["dev_type"] = dev_type

    if "npe" in result["os_type"].lower():
        return [result["dev_type"], result["os_type"], "NPE"]
    else:
        return [result["dev_type"], result["os_type"], "PE "]
