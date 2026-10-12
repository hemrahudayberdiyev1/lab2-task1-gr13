import os
import random
import shutil

data_dir = '/var/data'
result_file = '/var/result/data.txt'

files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f))]

if files:
    random_file = random.choice(files)
    shutil.copy2(os.path.join(data_dir, random_file), result_file)
    print(f"Файл '{random_file}' скопирован.")
else:
    print("Нет файлов в /var/data.")