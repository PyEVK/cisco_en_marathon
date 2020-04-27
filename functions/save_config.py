from datetime import date


def save_config(ssh, host_name, bkp_dir):
    today = date.today()
    config = ssh.send_command("show running-config")

    file_name = host_name + '_' + today.strftime("%Y-%m-%d") + ".txt"

    with open(bkp_dir + '/' + file_name, 'w') as file:
        file.write(config)
