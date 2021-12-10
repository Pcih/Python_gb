# Зададние 2
#
# *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
# превышает объем ОЗУ компьютера.


with open('nginx_logs.txt') as file:
    spam_dict = {}
    data = []
    row_data = []
    for num, row in enumerate(file):
        raw_row = row.split()
        row_data = [raw_row[0], raw_row[5].replace('"', ''), raw_row[6]]
        data.append(tuple(row_data))
        spam_dict.setdefault(raw_row[0], 0)
        spam_dict[raw_row[0]] += 1
spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
print(spam_dict[:5])
