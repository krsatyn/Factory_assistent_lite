import pandas as pd

# Чтение CSV-файла
df = pd.read_csv(r'dataset\dataset_v3_SGAU.csv')

print(df.to_json('file.json', orient ='split', compression = 'infer'))

# формирование сета данных

system_key = ''
user_request = 'Возник '
system_answer_head = 'Проблемма '
system_answer_tail = 'Она могла возникнуть из-за'
