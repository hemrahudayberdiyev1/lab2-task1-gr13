import os

data_file = '/var/data/data.txt'
result_file = '/var/result/result.txt'

if os.path.exists(data_file):
    with open(data_file, 'r') as f:
        content = f.read()
    
    numbers = [int(word) for word in content.split() if word.lstrip('-').isdigit()]
            
    if numbers:
        max_num = max(numbers)
        max_count = numbers.count(max_num)
        
        with open(result_file, 'w') as f:
            f.write(str(max_count))
            
        print(f"Наибольшее число: {max_num}. Количество: {max_count}")
    else:
        print("В файле нет целых чисел.")
else:
    print("Файл с исходными данными не найден.")