import os
import yaml
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from functions import *


# Окружение
# Рабочий каталог
work_dir = os.path.abspath(os.getcwd())
# каталог для сохранения конфигураций
backup_dir = work_dir + '/backups'

# расположение файла параметров подключения
devices_file_name = work_dir + "/conf/devices.yaml"

# максимаьлное количество одновременных подключений
worker_limit = 5


# Запуск скрипта
if __name__ == "__main__":
    # Чтение параметров подключения к оборудованию
    with open(devices_file_name) as devices_file:
        devices = yaml.safe_load(devices_file)

    # Создание каталога для конфигураций (если не создан)
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Запуск "домашнего задания" параллельно
    with ThreadPoolExecutor(max_workers=worker_limit) as executor:
        result = executor.map(home_task, devices, repeat(backup_dir))

    # Вывод на экран результатов работы
    for item in result:
        print(item)
