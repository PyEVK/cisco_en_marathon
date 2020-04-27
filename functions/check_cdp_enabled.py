import re


def check_cdp_enabled(ssh):
    regex = re.compile(r"CDP is not enabled")
    cmd_output = ssh.send_command('show cdp neighbors')
    match = regex.search(cmd_output)

    if match:
        return "CDP is OFF"
    else:
        regex = re.compile(
            r"(?P<r_dev>\w+)  +(?P<l_intf>\S+ \S+)"
            r"  +\d+  +[\w ]+  +\S+ +(?P<r_intf>\S+ \S+)"
        )

        nbr_count = 0
        for match in regex.finditer(cmd_output):
            nbr_count += 1

        return "CDP is ON,{} peers".format(nbr_count)
